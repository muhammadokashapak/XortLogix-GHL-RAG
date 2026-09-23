<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AuthController;
use App\Http\Controllers\ChatController;

/*
|--------------------------------------------------------------------------
| API Routes for GoHighLevel RAG Assistant (Laravel)
|--------------------------------------------------------------------------
*/

// System Status
Route::get('/status', function () {
    return response()->json([
        'status' => 'online',
        'backend' => 'PHP Laravel v11.x',
        'total_chunks' => 5379,
        'embedding_model' => 'nomic-embed-text-v1.5',
        'gemini_model' => 'gemini-3.5-flash',
        'has_default_key' => true
    ]);
});

// Authentication Routes
Route::post('/auth/signup', [AuthController::class, 'signup']);
Route::post('/auth/login', [AuthController::class, 'login']);

Route::middleware('auth:sanctum')->group(function () {
    Route::get('/auth/me', [AuthController::class, 'me']);
    Route::post('/auth/logout', [AuthController::class, 'logout']);
    Route::post('/auth/change-password', [AuthController::class, 'changePassword']);

    // Conversation History Routes
    Route::get('/conversations', [ChatController::class, 'index']);
    Route::post('/conversations', [ChatController::class, 'store']);
    Route::get('/conversations/{id}', [ChatController::class, 'show']);
    Route::put('/conversations/{id}', [ChatController::class, 'update']);
    Route::delete('/conversations/{id}', [ChatController::class, 'destroy']);
    Route::post('/conversations/{id}/pin', [ChatController::class, 'togglePin']);

    // RAG Chat Route
    Route::post('/chat', [ChatController::class, 'chat']);
});
