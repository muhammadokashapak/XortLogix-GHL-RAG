<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Conversation;
use App\Models\Message;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Str;

class ChatController extends Controller
{
    protected $ragMicroserviceUrl = 'http://127.0.0.1:7861/api/rag-search';

    public function index(Request $request)
    {
        $user = $request->user();
        $conversations = Conversation::where('user_id', $user->id)
            ->withCount('messages')
            ->orderBy('is_pinned', 'desc')
            ->orderBy('updated_at', 'desc')
            ->get();

        return response()->json(['conversations' => $conversations]);
    }

    public function store(Request $request)
    {
        $user = $request->user();
        $conv = Conversation::create([
            'id' => 'conv_' . Str::random(24),
            'user_id' => $user->id,
            'title' => 'New Chat',
            'is_pinned' => false,
        ]);

        return response()->json(['conversation' => $conv]);
    }

    public function show(Request $request, $id)
    {
        $user = $request->user();
        $conv = Conversation::where('id', $id)
            ->where('user_id', $user->id)
            ->with(['messages' => function ($q) {
                $q->orderBy('created_at', 'asc');
            }])
            ->first();

        if (!$conv) {
            return response()->json(['detail' => 'Conversation not found or access denied.'], 404);
        }

        return response()->json(['conversation' => $conv]);
    }

    public function update(Request $request, $id)
    {
        $request->validate(['title' => 'required|string|max:255']);
        $user = $request->user();

        $conv = Conversation::where('id', $id)->where('user_id', $user->id)->first();
        if (!$conv) {
            return response()->json(['detail' => 'Conversation not found or access denied.'], 404);
        }

        $conv->title = trim($request->title);
        $conv->save();

        return response()->json(['message' => 'Conversation renamed successfully', 'title' => $conv->title]);
    }

    public function togglePin(Request $request, $id)
    {
        $user = $request->user();
        $conv = Conversation::where('id', $id)->where('user_id', $user->id)->first();
        if (!$conv) {
            return response()->json(['detail' => 'Conversation not found or access denied.'], 404);
        }

        $conv->is_pinned = !$conv->is_pinned;
        $conv->save();

        return response()->json(['is_pinned' => $conv->is_pinned]);
    }

    public function destroy(Request $request, $id)
    {
        $user = $request->user();
        $conv = Conversation::where('id', $id)->where('user_id', $user->id)->first();
        if (!$conv) {
            return response()->json(['detail' => 'Conversation not found or access denied.'], 404);
        }

        $conv->messages()->delete();
        $conv->delete();

        return response()->json(['message' => 'Conversation deleted successfully']);
    }

    public function chat(Request $request)
    {
        $request->validate([
            'query' => 'required|string',
            'conversation_id' => 'nullable|string',
            'top_k' => 'nullable|integer',
            'api_key' => 'nullable|string',
        ]);

        $user = $request->user();
        $query = trim($request->query);
        $convId = $request->conversation_id;

        // 1. Resolve or Create Conversation
        $conv = null;
        if ($convId) {
            $conv = Conversation::where('id', $convId)->where('user_id', $user->id)->first();
        }

        if (!$conv) {
            $conv = Conversation::create([
                'id' => 'conv_' . Str::random(24),
                'user_id' => $user->id,
                'title' => 'New Chat',
                'is_pinned' => false,
            ]);
        }

        // 2. Save User Message
        Message::create([
            'id' => 'msg_' . Str::random(24),
            'conversation_id' => $conv->id,
            'role' => 'user',
            'content' => $query,
            'sources' => null,
        ]);

        // Auto-generate title if it's the first message
        if ($conv->title === 'New Chat' || empty($conv->title)) {
            $words = explode(' ', $query);
            $newTitle = count($words) > 6 ? implode(' ', array_slice($words, 0, 6)) . '...' : $query;
            $conv->title = Str::limit($newTitle, 45);
            $conv->save();
        }

        // 3. Call Python RAG Microservice (ChromaDB + Gemini 3.5 Flash)
        $startTime = microtime(true);
        $ragResponse = Http::post($this->ragMicroserviceUrl, [
            'query' => $query,
            'top_k' => $request->top_k ?? 4,
            'api_key' => $request->api_key ?? null,
        ]);

        if (!$ragResponse->successful()) {
            return response()->json(['detail' => 'RAG engine failed to generate answer.'], 500);
        }

        $ragData = $ragResponse->json();
        $answer = $ragData['answer'];
        $sources = $ragData['sources'] ?? [];

        // 4. Save Assistant Response
        Message::create([
            'id' => 'msg_' . Str::random(24),
            'conversation_id' => $conv->id,
            'role' => 'assistant',
            'content' => $answer,
            'sources' => json_encode($sources),
        ]);

        $conv->touch(); // Update updated_at timestamp

        $elapsedMs = round((microtime(true) - $startTime) * 1000, 2);

        return response()->json([
            'answer' => $answer,
            'sources' => $sources,
            'query_time_ms' => $elapsedMs,
            'top_k' => $request->top_k ?? 4,
            'conversation_id' => $conv->id,
            'conversation_title' => $conv->title,
            'model' => 'gemini-3.5-flash',
        ]);
    }
}
