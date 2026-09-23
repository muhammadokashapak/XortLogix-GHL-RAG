document.addEventListener('DOMContentLoaded', () => {
    // State Management
    let currentUser = null;
    let currentConversationId = null;
    let conversations = [];
    let activeDeleteId = null;
    let activeRenameId = null;

    let appSettings = {
        topK: 1
    };

    // DOM Elements - Auth
    const authWrapper = document.getElementById('auth-wrapper');
    const loginCard = document.getElementById('login-card');
    const loginForm = document.getElementById('login-form');
    const loginEmailInput = document.getElementById('login-email');
    const loginPasswordInput = document.getElementById('login-password');
    const loginErrorAlert = document.getElementById('login-error-alert');
    const loginSubmitBtn = document.getElementById('login-submit-btn');
    
    // DOM Elements - App & Sidebar
    const appView = document.getElementById('app-view');
    const sidebar = document.getElementById('sidebar');
    const sidebarOverlay = document.getElementById('sidebar-overlay');
    const sidebarCloseBtn = document.getElementById('sidebar-close-btn');
    const sidebarOpenBtn = document.getElementById('sidebar-open-btn');
    const newChatBtn = document.getElementById('new-chat-btn');
    const historyList = document.getElementById('history-list');
    const searchConversationsInput = document.getElementById('search-conversations-input');

    // User Profile Footer & Popover
    const userProfileTrigger = document.getElementById('user-profile-menu-trigger');
    const userAvatarInitials = document.getElementById('user-avatar-initials');
    const userDisplayName = document.getElementById('user-display-name');
    const userDisplayEmail = document.getElementById('user-display-email');
    const userAccountMenu = document.getElementById('user-account-menu');
    const openProfileMenuItem = document.getElementById('open-profile-menu-item');
    const logoutMenuItem = document.getElementById('logout-menu-item');

    // Chat Window & Multimodal Elements
    const activeChatTitle = document.getElementById('active-chat-title');
    const chatContainer = document.getElementById('chat-container');
    const welcomeScreen = document.getElementById('welcome-screen');
    const messagesList = document.getElementById('messages-list');
    const loadingIndicator = document.getElementById('loading-indicator');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const chunksCountBadge = document.getElementById('chunks-count-badge');

    // Floating Selection Reply Tooltip & Quote Preview Elements
    const selectionTooltip = document.getElementById('selection-reply-tooltip');
    const selectionReplyBtn = document.getElementById('selection-reply-btn');
    const quoteReplyPreview = document.getElementById('quote-reply-preview');
    const quoteReplyText = document.getElementById('quote-reply-text');
    const quoteCancelBtn = document.getElementById('quote-cancel-btn');
    let activeQuotedExcerpt = "";

    // Multimodal Elements
    const attachBtn = document.getElementById('attach-btn');
    const fileUploadInput = document.getElementById('file-upload-input');
    const voiceRecordBtn = document.getElementById('voice-record-btn');
    const attachmentsPreviewTray = document.getElementById('attachments-preview-tray');
    const voiceRecordingBar = document.getElementById('voice-recording-bar');
    const inputControlsRow = document.getElementById('input-controls-row');
    const recordingTimer = document.getElementById('recording-timer');
    const cancelRecordBtn = document.getElementById('cancel-record-btn');
    const sendRecordBtn = document.getElementById('send-record-btn');
    const dragDropOverlay = document.getElementById('drag-drop-overlay');
    const imageLightboxModal = document.getElementById('image-lightbox-modal');
    const lightboxImage = document.getElementById('lightbox-image');
    const lightboxCloseBtn = document.getElementById('lightbox-close-btn');

    let stagedAttachments = [];
    let mediaRecorder = null;
    let audioChunks = [];
    let recordingInterval = null;
    let recordingSeconds = 0;
    let activeAudioStream = null;

    // Unified Profile Modal Elements
    const profileModal = document.getElementById('profile-modal');
    const closeProfileModalBtn = document.getElementById('close-profile-modal');
    const modalAvatarInitials = document.getElementById('modal-avatar-initials');
    const editUserNameInput = document.getElementById('edit-user-name');
    const editUserEmailInput = document.getElementById('edit-user-email');
    const saveNameBtn = document.getElementById('save-name-btn');
    const profileErrorAlert = document.getElementById('profile-error-alert');
    const profileSuccessAlert = document.getElementById('profile-success-alert');
    const modalTabBtns = document.querySelectorAll('.modal-tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    // Password Elements
    const oldPwdInput = document.getElementById('old-pwd-input');
    const newPwdInput = document.getElementById('new-pwd-input');
    const confirmPwdInput = document.getElementById('confirm-pwd-input');
    const savePwdBtn = document.getElementById('save-pwd-btn');

    // Rename Modal
    const renameModal = document.getElementById('rename-modal');
    const renameInput = document.getElementById('rename-input');
    const closeRenameModalBtn = document.getElementById('close-rename-modal');
    const cancelRenameBtn = document.getElementById('cancel-rename');
    const saveRenameBtn = document.getElementById('save-rename');

    // Delete Modal
    const deleteModal = document.getElementById('delete-modal');
    const closeDeleteModalBtn = document.getElementById('close-delete-modal');
    const cancelDeleteBtn = document.getElementById('cancel-delete');
    const confirmDeleteBtn = document.getElementById('confirm-delete');
    const headerDeleteBtn = document.getElementById('header-delete-btn');

    // Configure Marked Markdown Renderer
    marked.setOptions({
        highlight: function (code, lang) {
            if (lang && hljs.getLanguage(lang)) {
                return hljs.highlight(code, { language: lang }).value;
            }
            return hljs.highlightAuto(code).value;
        },
        breaks: true
    });

    // Helper: Sanitize LaTeX / Math symbols and arrow commands into clean readable markdown/text
    function cleanLatexArtifacts(text) {
        if (!text || typeof text !== 'string') return text || '';
        let cleaned = text;

        // 1. Replace LaTeX Arrow Commands with Clean Unicode Arrows
        cleaned = cleaned.replace(/\\(rightarrow|longrightarrow|to|mapsto|implies)\b/g, '→');
        cleaned = cleaned.replace(/\\(leftarrow|longleftarrow)\b/g, '←');
        cleaned = cleaned.replace(/\\(Rightarrow|Longrightarrow)\b/g, '⇒');
        cleaned = cleaned.replace(/\\(Leftarrow|Longleftarrow)\b/g, '⇐');
        cleaned = cleaned.replace(/\\(leftrightarrow|longleftrightarrow)\b/g, '↔');
        cleaned = cleaned.replace(/\\(Leftrightarrow|Longleftrightarrow)\b/g, '⇔');
        cleaned = cleaned.replace(/\\(uparrow|Uparrow)\b/g, '↑');
        cleaned = cleaned.replace(/\\(downarrow|Downarrow)\b/g, '↓');

        // 2. Replace LaTeX comparison/math operators
        cleaned = cleaned.replace(/\\ge\b/g, '>=');
        cleaned = cleaned.replace(/\\le\b/g, '<=');
        cleaned = cleaned.replace(/\\geq\b/g, '>=');
        cleaned = cleaned.replace(/\\leq\b/g, '<=');
        cleaned = cleaned.replace(/\\neq\b/g, '!=');
        cleaned = cleaned.replace(/\\ne\b/g, '!=');
        cleaned = cleaned.replace(/\\times\b/g, '*');
        cleaned = cleaned.replace(/\\approx\b/g, '≈');
        cleaned = cleaned.replace(/\\pm\b/g, '±');
        cleaned = cleaned.replace(/\\cdot\b/g, '*');

        // 3. Clean \text{...}, \textbf{...}, \mathrm{...}, etc.
        cleaned = cleaned.replace(/\\textbf\{([^{}]+)\}/g, '**$1**');
        cleaned = cleaned.replace(/\\text\{([^{}]+)\}/g, '$1');
        cleaned = cleaned.replace(/\\mathrm\{([^{}]+)\}/g, '$1');
        cleaned = cleaned.replace(/\\mathbf\{([^{}]+)\}/g, '$1');
        cleaned = cleaned.replace(/\\mathit\{([^{}]+)\}/g, '$1');

        // 4. Clean fractions \frac{a}{b} -> (a / b)
        cleaned = cleaned.replace(/\\frac\{([^{}]+)\}\{([^{}]+)\}/g, '($1 / $2)');

        // 5. Strip remaining backslashes from common math keywords
        cleaned = cleaned.replace(/\\(min|max|log|ln|sin|cos|tan|sum|prod|int|sqrt)\b/g, '$1');

        // 6. Replace $$...$$ or $...$ with clean code formatting
        cleaned = cleaned.replace(/\$\$([\s\S]+?)\$\$/g, (match, p1) => {
            const inner = p1.trim();
            return inner.includes('\n') ? `\n\`\`\`\n${inner}\n\`\`\`\n` : `\`${inner}\``;
        });
        cleaned = cleaned.replace(/\$([^\$\n]+?)\$/g, '`$1`');
        cleaned = cleaned.replace(/\$\$/g, '');

        return cleaned;
    }

    function renderMarkdown(text) {
        return marked.parse(cleanLatexArtifacts(text));
    }

    // Helper: Authenticated Fetch (Persists across browser refreshes)
    async function authFetch(url, options = {}) {
        options = options || {};
        options.headers = options.headers || {};
        
        const token = localStorage.getItem('ghl_session_token');
        if (token) {
            options.headers['Authorization'] = `Bearer ${token}`;
        }
        
        return fetch(url, options);
    }
    window.authFetch = authFetch;

    // Initialize App Session
    checkAuthSession();
    fetchSystemStatus();

    // ==========================================
    // AUTHENTICATION FLOW
    // ==========================================
    async function checkAuthSession() {
        try {
            const res = await authFetch('/api/auth/me');
            if (res.ok) {
                const data = await res.json();
                currentUser = data.user;
                showAppView();
            } else {
                localStorage.removeItem('ghl_session_token');
                currentUser = null;
                showAuthView();
            }
        } catch (err) {
            showAuthView();
        }
    }

    function showAuthView() {
        authWrapper.classList.remove('hidden');
        appView.classList.add('hidden');
    }

    function showAppView() {
        authWrapper.classList.add('hidden');
        if (currentUser && currentUser.email === 'muhammad.okasha2146@gmail.com') {
            appView.classList.add('hidden');
            document.getElementById('admin-view').classList.remove('hidden');
            loadAdminUsers();
        } else {
            document.getElementById('admin-view').classList.add('hidden');
            appView.classList.remove('hidden');
            
            // Update User Profile Details
            if (currentUser) {
                userDisplayName.textContent = currentUser.name;
                userDisplayEmail.textContent = currentUser.email;
                userAvatarInitials.textContent = currentUser.name.charAt(0).toUpperCase();
            }

            // Fetch Conversations
            loadConversations();
        }
    }

    
    // Password Visibility Toggles
    document.querySelectorAll('.toggle-password-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-target');
            const targetInput = document.getElementById(targetId);
            if (targetInput) {
                targetInput.type = targetInput.type === 'password' ? 'text' : 'password';
            }
        });
    });

    function clearAuthAlerts() {
        loginErrorAlert.classList.add('hidden');
    }

    // Login Form Submit
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        clearAuthAlerts();

        const email = loginEmailInput.value.trim();
        const password = loginPasswordInput.value;

        if (!email || !password) {
            loginErrorAlert.textContent = 'Please enter both email and password.';
            loginErrorAlert.classList.remove('hidden');
            return;
        }

        setAuthLoading(loginSubmitBtn, true);

        try {
            const res = await fetch('/api/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            const data = await res.json();
            setAuthLoading(loginSubmitBtn, false);

            if (!res.ok) {
                loginErrorAlert.textContent = data.detail || 'Login failed. Please check your credentials.';
                loginErrorAlert.classList.remove('hidden');
            } else {
                if (data.token) {
                    localStorage.setItem('ghl_session_token', data.token);
                }
                currentUser = data.user;
                showAppView();
            }
        } catch (err) {
            setAuthLoading(loginSubmitBtn, false);
            loginErrorAlert.textContent = 'Connection error. Please try again.';
            loginErrorAlert.classList.remove('hidden');
        }
    });

    function setAuthLoading(btn, isLoading) {
        const text = btn.querySelector('.btn-text');
        const spinner = btn.querySelector('.btn-spinner');
        if (isLoading) {
            btn.disabled = true;
            text.classList.add('hidden');
            spinner.classList.remove('hidden');
        } else {
            btn.disabled = false;
            text.classList.remove('hidden');
            spinner.classList.add('hidden');
        }
    }

    // User Account Popover Menu
    userProfileTrigger.addEventListener('click', (e) => {
        e.stopPropagation();
        userAccountMenu.classList.toggle('hidden');
    });

    document.addEventListener('click', (e) => {
        if (!userProfileTrigger.contains(e.target) && !userAccountMenu.contains(e.target)) {
            userAccountMenu.classList.add('hidden');
        }
    });

    logoutMenuItem.addEventListener('click', async () => {
        try {
            await authFetch('/api/auth/logout', { method: 'POST' });
        } catch (e) {}
        localStorage.removeItem('ghl_session_token');
        currentUser = null;
        currentConversationId = null;
        userAccountMenu.classList.add('hidden');
        showAuthView();
    });

    // ==========================================
    // CONVERSATIONS & CHAT HISTORY
    // ==========================================
    async function loadConversations() {
        try {
            const res = await authFetch('/api/conversations');
            if (res.ok) {
                const data = await res.json();
                conversations = data.conversations;
                renderConversationSidebar(conversations);

                // Auto-restore last active conversation on page load / refresh
                if (!currentConversationId && conversations && conversations.length > 0) {
                    const savedConvId = localStorage.getItem('ghl_active_conv_id');
                    if (savedConvId && conversations.some(c => c.id === savedConvId)) {
                        openConversation(savedConvId);
                    } else {
                        openConversation(conversations[0].id);
                    }
                }
            }
        } catch (err) {
            console.error('Failed to load conversations:', err);
        }
    }

    function renderConversationSidebar(convList) {
        historyList.innerHTML = '';

        if (!convList || convList.length === 0) {
            historyList.innerHTML = `<div class="empty-history-text">No conversations yet. Click <strong>+ New Chat</strong> to start!</div>`;
            return;
        }

        // Group by Date Categories
        const groups = {
            pinned: [],
            today: [],
            yesterday: [],
            previous7Days: [],
            older: []
        };

        const now = new Date();
        const todayStr = now.toDateString();
        
        const yesterday = new Date(now);
        yesterday.setDate(yesterday.getDate() - 1);
        const yesterdayStr = yesterday.toDateString();

        const sevenDaysAgo = new Date(now);
        sevenDaysAgo.setDate(sevenDaysAgo.getDate() - 7);

        convList.forEach(c => {
            if (c.is_pinned) {
                groups.pinned.push(c);
                return;
            }
            const date = new Date(c.updated_at);
            const dateStr = date.toDateString();

            if (dateStr === todayStr) {
                groups.today.push(c);
            } else if (dateStr === yesterdayStr) {
                groups.yesterday.push(c);
            } else if (date >= sevenDaysAgo) {
                groups.previous7Days.push(c);
            } else {
                groups.older.push(c);
            }
        });

        renderGroupSection('PINNED', groups.pinned);
        renderGroupSection('TODAY', groups.today);
        renderGroupSection('YESTERDAY', groups.yesterday);
        renderGroupSection('PREVIOUS 7 DAYS', groups.previous7Days);
        renderGroupSection('OLDER', groups.older);
    }

    function renderGroupSection(title, items) {
        if (!items || items.length === 0) return;

        const header = document.createElement('div');
        header.className = 'history-date-header';
        header.textContent = title;
        historyList.appendChild(header);

        items.forEach(c => {
            const item = document.createElement('div');
            item.className = `history-item ${c.id === currentConversationId ? 'active' : ''}`;
            item.setAttribute('data-id', c.id);

            item.innerHTML = `
                <div class="history-title-wrapper">
                    ${c.is_pinned ? '<span class="pin-icon">📌</span>' : ''}
                    <span class="history-title-text">${escapeHtml(c.title)}</span>
                </div>
                <div class="history-item-actions">
                    <button class="action-icon-btn pin-btn" title="${c.is_pinned ? 'Unpin' : 'Pin'}">📌</button>
                    <button class="action-icon-btn rename-btn" title="Rename">✏️</button>
                    <button class="action-icon-btn delete-btn" title="Delete">🗑️</button>
                </div>
            `;

            // Open Conversation Click
            item.addEventListener('click', (e) => {
                if (e.target.closest('.action-icon-btn')) return;
                openConversation(c.id);
            });

            // Action Buttons
            const pinBtn = item.querySelector('.pin-btn');
            const renameBtn = item.querySelector('.rename-btn');
            const deleteBtn = item.querySelector('.delete-btn');

            pinBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                togglePin(c.id);
            });

            renameBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                openRenameModal(c.id, c.title);
            });

            deleteBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                openDeleteModal(c.id);
            });

            historyList.appendChild(item);
        });
    }

    // Search Filter
    searchConversationsInput.addEventListener('input', () => {
        const query = searchConversationsInput.value.toLowerCase().trim();
        if (!query) {
            renderConversationSidebar(conversations);
            return;
        }
        const filtered = conversations.filter(c => c.title.toLowerCase().includes(query));
        renderConversationSidebar(filtered);
    });

    // Start New Chat
    newChatBtn.addEventListener('click', startNewChat);

    function startNewChat() {
        currentConversationId = null;
        localStorage.removeItem('ghl_active_conv_id');
        messagesList.innerHTML = '';
        welcomeScreen.classList.remove('hidden');
        if (activeChatTitle) {
            activeChatTitle.textContent = 'XortLogix High Level Assistant';
        }
        if (headerDeleteBtn) {
            headerDeleteBtn.classList.add('hidden');
        }

        // Reset staged attachments
        stagedAttachments = [];
        renderAttachmentsTray();

        // Reset quoted selection
        activeQuotedExcerpt = "";
        if (quoteReplyPreview) quoteReplyPreview.classList.add('hidden');
        if (userInput) userInput.placeholder = "Message XortLogix High Level Assistant...";

        // Update active class in sidebar
        document.querySelectorAll('.history-item').forEach(el => el.classList.remove('active'));

        // Close sidebar on mobile
        if (window.innerWidth <= 768) {
            closeSidebar();
        }
    }

    // Scroll directly to the last message sent by user
    function scrollToLastUserMessage() {
        if (!messagesList) return;
        const userMsgs = messagesList.querySelectorAll('.message-wrapper.user');
        if (userMsgs.length > 0) {
            const lastMsg = userMsgs[userMsgs.length - 1];
            setTimeout(() => {
                lastMsg.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 80);
        } else {
            scrollToBottom();
        }
    }

    // Open Existing Conversation
    async function openConversation(convId) {
        currentConversationId = convId;
        localStorage.setItem('ghl_active_conv_id', convId);
        welcomeScreen.classList.add('hidden');
        messagesList.innerHTML = '';
        if (headerDeleteBtn) {
            headerDeleteBtn.classList.remove('hidden');
        }

        // Reset staged attachments
        stagedAttachments = [];
        renderAttachmentsTray();

        // Reset quoted selection
        activeQuotedExcerpt = "";
        if (quoteReplyPreview) quoteReplyPreview.classList.add('hidden');
        if (userInput) userInput.placeholder = "Message XortLogix High Level Assistant...";

        // Highlight Active in Sidebar
        document.querySelectorAll('.history-item').forEach(el => {
            if (el.getAttribute('data-id') === convId) {
                el.classList.add('active');
            } else {
                el.classList.remove('active');
            }
        });

        // Close sidebar on mobile
        if (window.innerWidth <= 768) {
            closeSidebar();
        }

        try {
            const res = await authFetch(`/api/conversations/${convId}`);
            if (res.ok) {
                const data = await res.json();
                const conv = data.conversation;

                if (activeChatTitle) {
                    activeChatTitle.textContent = conv.title;
                }

                conv.messages.forEach(msg => {
                    appendMessageToDOM(msg.role, msg.content, msg.sources || [], false, msg.attachments || []);
                });

                // Smoothly position screen starting at user's last message
                scrollToLastUserMessage();
            }
        } catch (err) {
            console.error('Failed to load conversation details:', err);
        }
    }

    // Toggle Pin
    async function togglePin(convId) {
        try {
            await authFetch(`/api/conversations/${convId}/pin`, { method: 'POST' });
            loadConversations();
        } catch (err) {
            console.error('Pin toggle failed:', err);
        }
    }

    // Rename Conversation Modal
    function openRenameModal(convId, currentTitle) {
        activeRenameId = convId;
        renameInput.value = currentTitle;
        if (renameModal) {
            renameModal.classList.remove('hidden');
        }
        setTimeout(() => renameInput && renameInput.focus(), 50);
    }
    window.openRenameModal = openRenameModal;

    closeRenameModalBtn.addEventListener('click', () => {
        if (renameModal) renameModal.classList.add('hidden');
        activeRenameId = null;
    });
    cancelRenameBtn.addEventListener('click', () => {
        if (renameModal) renameModal.classList.add('hidden');
        activeRenameId = null;
    });

    if (renameModal) {
        renameModal.addEventListener('click', (e) => {
            if (e.target === renameModal) {
                renameModal.classList.add('hidden');
                activeRenameId = null;
            }
        });
    }

    saveRenameBtn.addEventListener('click', async () => {
        const newTitle = renameInput.value.trim();
        if (!newTitle || !activeRenameId) return;

        try {
            saveRenameBtn.disabled = true;
            await authFetch(`/api/conversations/${activeRenameId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ title: newTitle })
            });

            if (renameModal) renameModal.classList.add('hidden');
            if (currentConversationId === activeRenameId && activeChatTitle) {
                activeChatTitle.textContent = newTitle;
            }
            activeRenameId = null;
            loadConversations();
        } catch (err) {
            console.error('Rename failed:', err);
        } finally {
            saveRenameBtn.disabled = false;
        }
    });

    // Delete Conversation Modal
    function openDeleteModal(convId) {
        if (!convId) return;
        activeDeleteId = convId;
        if (deleteModal) {
            deleteModal.classList.remove('hidden');
        }
    }
    window.openDeleteModal = openDeleteModal;

    if (headerDeleteBtn) {
        headerDeleteBtn.addEventListener('click', () => {
            if (currentConversationId) {
                openDeleteModal(currentConversationId);
            }
        });
    }

    closeDeleteModalBtn.addEventListener('click', () => {
        if (deleteModal) deleteModal.classList.add('hidden');
        activeDeleteId = null;
    });
    cancelDeleteBtn.addEventListener('click', () => {
        if (deleteModal) deleteModal.classList.add('hidden');
        activeDeleteId = null;
    });

    if (deleteModal) {
        deleteModal.addEventListener('click', (e) => {
            if (e.target === deleteModal) {
                deleteModal.classList.add('hidden');
                activeDeleteId = null;
            }
        });
    }

    // Global ESC key handler to close modals
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            if (deleteModal) deleteModal.classList.add('hidden');
            if (renameModal) renameModal.classList.add('hidden');
            if (profileModal) profileModal.classList.add('hidden');
            activeDeleteId = null;
            activeRenameId = null;
        }
    });

    confirmDeleteBtn.addEventListener('click', async () => {
        if (!activeDeleteId) return;

        const idToDelete = activeDeleteId;
        try {
            confirmDeleteBtn.disabled = true;
            confirmDeleteBtn.textContent = 'Deleting...';

            const res = await authFetch(`/api/conversations/${idToDelete}`, { method: 'DELETE' });
            if (!res.ok) {
                await authFetch(`/conversations/${idToDelete}`, { method: 'DELETE' });
            }

            if (deleteModal) {
                deleteModal.classList.add('hidden');
            }

            // Optimistic UI update
            conversations = (conversations || []).filter(c => c.id !== idToDelete);
            renderConversationSidebar(conversations);

            if (currentConversationId === idToDelete) {
                startNewChat();
            }
            activeDeleteId = null;
            await loadConversations();
        } catch (err) {
            console.error('Delete failed:', err);
            alert('Failed to delete conversation: ' + err.message);
        } finally {
            confirmDeleteBtn.disabled = false;
            confirmDeleteBtn.textContent = 'Delete Permanent';
        }
    });

    // ==========================================
    // UNIFIED PROFILE & PREFERENCES MODAL
    // ==========================================
    function openProfileModal(initialTab = 'tab-identity') {
        if (!currentUser) return;
        userAccountMenu.classList.add('hidden');
        
        // Populate Personal Info
        if (editUserNameInput) editUserNameInput.value = currentUser.name || '';
        if (editUserEmailInput) editUserEmailInput.value = currentUser.email || '';
        if (modalAvatarInitials) {
            modalAvatarInitials.textContent = (currentUser.name || 'U').charAt(0).toUpperCase();
        }

        // Clear Password fields & alerts
        if (oldPwdInput) oldPwdInput.value = '';
        if (newPwdInput) newPwdInput.value = '';
        if (confirmPwdInput) confirmPwdInput.value = '';
        clearProfileAlerts();

        // Switch to initial tab
        switchProfileTab(initialTab);

        if (profileModal) {
            profileModal.classList.remove('hidden');
        }
    }
    window.openProfileModal = openProfileModal;

    function switchProfileTab(tabId) {
        modalTabBtns.forEach(btn => {
            if (btn.getAttribute('data-tab') === tabId) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
        tabPanes.forEach(pane => {
            if (pane.id === tabId) {
                pane.classList.remove('hidden');
            } else {
                pane.classList.add('hidden');
            }
        });
        clearProfileAlerts();
    }

    modalTabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.getAttribute('data-tab');
            switchProfileTab(tabId);
        });
    });

    function clearProfileAlerts() {
        if (profileErrorAlert) profileErrorAlert.classList.add('hidden');
        if (profileSuccessAlert) profileSuccessAlert.classList.add('hidden');
    }

    function showProfileError(msg) {
        if (profileSuccessAlert) profileSuccessAlert.classList.add('hidden');
        if (profileErrorAlert) {
            profileErrorAlert.textContent = msg;
            profileErrorAlert.classList.remove('hidden');
        }
    }

    function showProfileSuccess(msg) {
        if (profileErrorAlert) profileErrorAlert.classList.add('hidden');
        if (profileSuccessAlert) {
            profileSuccessAlert.textContent = msg;
            profileSuccessAlert.classList.remove('hidden');
        }
    }

    if (openProfileMenuItem) {
        openProfileMenuItem.addEventListener('click', () => openProfileModal('tab-identity'));
    }

    if (closeProfileModalBtn) {
        closeProfileModalBtn.addEventListener('click', () => {
            if (profileModal) profileModal.classList.add('hidden');
        });
    }

    if (profileModal) {
        profileModal.addEventListener('click', (e) => {
            if (e.target === profileModal) {
                profileModal.classList.add('hidden');
            }
        });
    }

    // Save Name Handler
    if (saveNameBtn) {
        saveNameBtn.addEventListener('click', async () => {
            const newName = editUserNameInput.value.trim();
            if (!newName) {
                showProfileError('Please enter a valid full name.');
                return;
            }

            setBtnLoading(saveNameBtn, true);
            clearProfileAlerts();

            try {
                const res = await authFetch('/api/auth/update-profile', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name: newName })
                });
                const data = await res.json();
                setBtnLoading(saveNameBtn, false);

                if (!res.ok) {
                    showProfileError(data.detail || 'Failed to update profile.');
                } else {
                    currentUser.name = newName;
                    userDisplayName.textContent = newName;
                    const initial = newName.charAt(0).toUpperCase();
                    userAvatarInitials.textContent = initial;
                    if (modalAvatarInitials) modalAvatarInitials.textContent = initial;
                    showProfileSuccess('Profile name updated successfully!');
                }
            } catch (err) {
                setBtnLoading(saveNameBtn, false);
                showProfileError('Connection error. Please try again.');
            }
        });
    }

    // Save Password Handler
    if (savePwdBtn) {
        savePwdBtn.addEventListener('click', async () => {
            const old_password = oldPwdInput.value;
            const new_password = newPwdInput.value;
            const confirm_password = confirmPwdInput ? confirmPwdInput.value : new_password;

            clearProfileAlerts();

            if (!old_password || !new_password) {
                showProfileError('Please fill out all password fields.');
                return;
            }

            if (new_password.length < 6) {
                showProfileError('New password must be at least 6 characters.');
                return;
            }

            if (new_password !== confirm_password) {
                showProfileError('New passwords do not match.');
                return;
            }

            setBtnLoading(savePwdBtn, true);

            try {
                const res = await authFetch('/api/auth/change-password', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ old_password, new_password })
                });
                const data = await res.json();
                setBtnLoading(savePwdBtn, false);

                if (!res.ok) {
                    showProfileError(data.detail || 'Password update failed.');
                } else {
                    showProfileSuccess('Password updated successfully!');
                    oldPwdInput.value = '';
                    newPwdInput.value = '';
                    if (confirmPwdInput) confirmPwdInput.value = '';
                }
            } catch (err) {
                setBtnLoading(savePwdBtn, false);
                showProfileError('Connection error. Please try again.');
            }
        });
    }

    function setBtnLoading(btn, isLoading) {
        if (!btn) return;
        const text = btn.querySelector('.btn-text');
        const spinner = btn.querySelector('.btn-spinner');
        if (isLoading) {
            btn.disabled = true;
            if (text) text.classList.add('hidden');
            if (spinner) spinner.classList.remove('hidden');
        } else {
            btn.disabled = false;
            if (text) text.classList.remove('hidden');
            if (spinner) spinner.classList.add('hidden');
        }
    }


    // ==========================================
    // MULTIMODAL ATTACHMENTS & VOICE RECORDING
    // ==========================================

    function updateSendButtonState() {
        if (!sendBtn) return;
        const hasText = userInput.value.trim().length > 0;
        const hasAttachments = stagedAttachments.length > 0;
        sendBtn.disabled = !hasText && !hasAttachments;
    }

    function formatFileSize(bytes) {
        if (!bytes || bytes === 0) return '0 B';
        const k = 1024;
        const sizes = ['B', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
    }

    function renderAttachmentsTray() {
        if (!attachmentsPreviewTray) return;
        if (stagedAttachments.length === 0) {
            attachmentsPreviewTray.classList.add('hidden');
            attachmentsPreviewTray.innerHTML = '';
            updateSendButtonState();
            return;
        }

        attachmentsPreviewTray.classList.remove('hidden');
        attachmentsPreviewTray.innerHTML = '';

        stagedAttachments.forEach((att, index) => {
            const card = document.createElement('div');
            
            if (att.type === 'image') {
                card.className = 'attachment-preview-card image-card';
                card.innerHTML = `
                    <img src="${att.data}" alt="${escapeHtml(att.name)}" title="${escapeHtml(att.name)}">
                    <button type="button" class="attachment-remove-btn" data-index="${index}" title="Remove image">✕</button>
                `;
            } else if (att.type === 'audio') {
                card.className = 'attachment-preview-card';
                card.innerHTML = `
                    <span style="font-size:16px;">🎙️</span>
                    <div class="attachment-card-info">
                        <span class="attachment-card-name">${escapeHtml(att.name)}</span>
                        <span class="attachment-card-meta">Voice Audio (${formatFileSize(att.size)})</span>
                    </div>
                    <button type="button" class="attachment-remove-btn" data-index="${index}" title="Remove audio">✕</button>
                `;
            } else {
                card.className = 'attachment-preview-card';
                card.innerHTML = `
                    <span style="font-size:16px;">📄</span>
                    <div class="attachment-card-info">
                        <span class="attachment-card-name">${escapeHtml(att.name)}</span>
                        <span class="attachment-card-meta">${formatFileSize(att.size)}</span>
                    </div>
                    <button type="button" class="attachment-remove-btn" data-index="${index}" title="Remove file">✕</button>
                `;
            }

            const removeBtn = card.querySelector('.attachment-remove-btn');
            if (removeBtn) {
                removeBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    stagedAttachments.splice(index, 1);
                    renderAttachmentsTray();
                });
            }

            attachmentsPreviewTray.appendChild(card);
        });

        updateSendButtonState();
    }

    async function processFile(file) {
        if (!file) return;

        // Size limit check (25MB)
        if (file.size > 25 * 1024 * 1024) {
            alert(`File "${file.name}" is too large. Maximum size is 25MB.`);
            return;
        }

        let fileType = 'document';
        if (file.type.startsWith('image/')) {
            fileType = 'image';
        } else if (file.type.startsWith('audio/') || file.name.endsWith('.m4a') || file.name.endsWith('.wav') || file.name.endsWith('.mp3')) {
            fileType = 'audio';
        }

        return new Promise((resolve) => {
            const reader = new FileReader();
            reader.onload = () => {
                const base64Data = reader.result;
                stagedAttachments.push({
                    name: file.name,
                    type: fileType,
                    mime_type: file.type || 'application/octet-stream',
                    size: file.size,
                    data: base64Data
                });
                renderAttachmentsTray();
                resolve();
            };
            reader.readAsDataURL(file);
        });
    }

    async function handleFilesSelected(files) {
        if (!files || files.length === 0) return;
        for (let i = 0; i < files.length; i++) {
            await processFile(files[i]);
        }
        if (fileUploadInput) fileUploadInput.value = '';
    }

    if (attachBtn && fileUploadInput) {
        attachBtn.addEventListener('click', () => {
            fileUploadInput.click();
        });

        fileUploadInput.addEventListener('change', (e) => {
            handleFilesSelected(e.target.files);
        });
    }

    // Clipboard Paste Listener (Ctrl+V / Cmd+V screenshot or file paste)
    document.addEventListener('paste', async (e) => {
        if (!e.clipboardData || !e.clipboardData.items) return;
        const items = e.clipboardData.items;
        let fileFound = false;

        for (let i = 0; i < items.length; i++) {
            const item = items[i];
            if (item.kind === 'file') {
                const file = item.getAsFile();
                if (file) {
                    fileFound = true;
                    // Provide friendly name for pasted screenshots
                    const customFile = file.name && file.name !== 'image.png' 
                        ? file 
                        : new File([file], `screenshot_${Date.now()}.png`, { type: file.type || 'image/png' });
                    await processFile(customFile);
                }
            }
        }
    });

    // Drag and Drop Listeners
    window.addEventListener('dragover', (e) => {
        e.preventDefault();
        if (dragDropOverlay) dragDropOverlay.classList.remove('hidden');
    });

    if (dragDropOverlay) {
        dragDropOverlay.addEventListener('dragleave', (e) => {
            e.preventDefault();
            dragDropOverlay.classList.add('hidden');
        });

        dragDropOverlay.addEventListener('drop', (e) => {
            e.preventDefault();
            dragDropOverlay.classList.add('hidden');
            if (e.dataTransfer && e.dataTransfer.files) {
                handleFilesSelected(e.dataTransfer.files);
            }
        });
    }

    // Voice Recording Engine
    async function startVoiceRecording() {
        try {
            if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
                alert('Microphone access is not supported by your browser or environment.');
                return;
            }

            activeAudioStream = await navigator.mediaDevices.getUserMedia({ audio: true });
            audioChunks = [];

            const options = { mimeType: 'audio/webm' };
            if (!MediaRecorder.isTypeSupported('audio/webm')) {
                delete options.mimeType;
            }

            mediaRecorder = new MediaRecorder(activeAudioStream, options);

            mediaRecorder.ondataavailable = (event) => {
                if (event.data && event.data.size > 0) {
                    audioChunks.push(event.data);
                }
            };

            mediaRecorder.onstop = () => {
                if (audioChunks.length > 0) {
                    const audioBlob = new Blob(audioChunks, { type: mediaRecorder.mimeType || 'audio/webm' });
                    const reader = new FileReader();
                    reader.onload = () => {
                        stagedAttachments.push({
                            name: `voice_note_${Date.now()}.webm`,
                            type: 'audio',
                            mime_type: audioBlob.type || 'audio/webm',
                            size: audioBlob.size,
                            data: reader.result
                        });
                        renderAttachmentsTray();
                    };
                    reader.readAsDataURL(audioBlob);
                }
                stopMediaStream();
            };

            mediaRecorder.start();
            recordingSeconds = 0;
            updateRecordingTimer();

            if (recordingInterval) clearInterval(recordingInterval);
            recordingInterval = setInterval(() => {
                recordingSeconds++;
                updateRecordingTimer();
            }, 1000);

            // Switch UI to voice recording bar
            if (voiceRecordingBar) voiceRecordingBar.classList.remove('hidden');
            if (inputControlsRow) inputControlsRow.classList.add('hidden');
            if (voiceRecordBtn) voiceRecordBtn.classList.add('recording-active');

        } catch (err) {
            console.error('Microphone permission error:', err);
            alert('Unable to access microphone. Please grant microphone permissions in browser settings.');
        }
    }

    function stopVoiceRecording(save = true) {
        if (recordingInterval) {
            clearInterval(recordingInterval);
            recordingInterval = null;
        }

        if (mediaRecorder && mediaRecorder.state !== 'inactive') {
            if (!save) {
                audioChunks = []; // Clear so onstop discards
            }
            mediaRecorder.stop();
        } else {
            stopMediaStream();
        }

        // Restore regular input controls row
        if (voiceRecordingBar) voiceRecordingBar.classList.add('hidden');
        if (inputControlsRow) inputControlsRow.classList.remove('hidden');
        if (voiceRecordBtn) voiceRecordBtn.classList.remove('recording-active');
    }

    function stopMediaStream() {
        if (activeAudioStream) {
            activeAudioStream.getTracks().forEach(track => track.stop());
            activeAudioStream = null;
        }
    }

    function updateRecordingTimer() {
        if (!recordingTimer) return;
        const mins = Math.floor(recordingSeconds / 60);
        const secs = recordingSeconds % 60;
        recordingTimer.textContent = `${mins}:${secs < 10 ? '0' : ''}${secs}`;
    }

    if (voiceRecordBtn) {
        voiceRecordBtn.addEventListener('click', () => {
            if (mediaRecorder && mediaRecorder.state === 'recording') {
                stopVoiceRecording(true);
            } else {
                startVoiceRecording();
            }
        });
    }

    if (cancelRecordBtn) {
        cancelRecordBtn.addEventListener('click', () => {
            stopVoiceRecording(false);
        });
    }

    if (sendRecordBtn) {
        sendRecordBtn.addEventListener('click', () => {
            stopVoiceRecording(true);
        });
    }

    // Lightbox Image Viewer
    function openImageLightbox(src) {
        if (!imageLightboxModal || !lightboxImage) return;
        lightboxImage.src = src;
        imageLightboxModal.classList.remove('hidden');
    }

    if (lightboxCloseBtn && imageLightboxModal) {
        lightboxCloseBtn.addEventListener('click', () => {
            imageLightboxModal.classList.add('hidden');
            lightboxImage.src = '';
        });

        imageLightboxModal.addEventListener('click', (e) => {
            if (e.target === imageLightboxModal) {
                imageLightboxModal.classList.add('hidden');
                lightboxImage.src = '';
            }
        });
    }

    // ==========================================
    // CHAT EXECUTION & RAG PIPELINE
    // ==========================================

    // ChatGPT-Style Text Selection Tooltip & Quote Reply Handlers
    document.addEventListener('mouseup', handleSelectionEvent);
    document.addEventListener('touchend', handleSelectionEvent);
    document.addEventListener('selectionchange', handleSelectionDebounced);

    let selectionDebounceTimer = null;
    function handleSelectionDebounced() {
        clearTimeout(selectionDebounceTimer);
        selectionDebounceTimer = setTimeout(handleSelectionEvent, 80);
    }

    function handleSelectionEvent() {
        const sel = window.getSelection();
        if (!sel || sel.isCollapsed) {
            hideSelectionTooltip();
            return;
        }

        const text = sel.toString().trim();
        if (text.length < 3) {
            hideSelectionTooltip();
            return;
        }

        // Only show tooltip if selection is within markdown content in assistant messages
        const node = sel.anchorNode;
        const elem = node ? (node.nodeType === Node.ELEMENT_NODE ? node : node.parentElement) : null;
        if (!elem || !elem.closest('.markdown-content, .assistant-body')) {
            hideSelectionTooltip();
            return;
        }

        try {
            const range = sel.getRangeAt(0);
            const rect = range.getBoundingClientRect();
            if (rect.width === 0 && rect.height === 0) {
                hideSelectionTooltip();
                return;
            }

            if (selectionTooltip) {
                selectionTooltip.style.left = `${rect.left + rect.width / 2}px`;
                selectionTooltip.style.top = `${rect.top - 6}px`;
                selectionTooltip.classList.remove('hidden');
            }
        } catch (e) {
            hideSelectionTooltip();
        }
    }

    function hideSelectionTooltip() {
        if (selectionTooltip && !selectionTooltip.classList.contains('hidden')) {
            selectionTooltip.classList.add('hidden');
        }
    }

    if (selectionReplyBtn) {
        selectionReplyBtn.addEventListener('mousedown', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const sel = window.getSelection();
            const text = sel ? sel.toString().trim() : '';
            if (!text) return;

            activeQuotedExcerpt = text;
            if (quoteReplyText) quoteReplyText.textContent = `"${text}"`;
            if (quoteReplyPreview) quoteReplyPreview.classList.remove('hidden');

            sel.removeAllRanges();
            hideSelectionTooltip();

            if (userInput) {
                userInput.focus();
                userInput.placeholder = "Ask a question about this excerpt...";
            }
        });
    }

    if (quoteCancelBtn) {
        quoteCancelBtn.addEventListener('click', () => {
            activeQuotedExcerpt = "";
            if (quoteReplyPreview) quoteReplyPreview.classList.add('hidden');
            if (quoteReplyText) quoteReplyText.textContent = "";
            if (userInput) userInput.placeholder = "Message XortLogix High Level Assistant...";
        });
    }

    userInput.addEventListener('input', () => {
        autoResizeTextarea();
        updateSendButtonState();
    });

    userInput.addEventListener('focus', () => {
        setTimeout(scrollToBottom, 250);
    });

    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    });

    sendBtn.addEventListener('click', handleSendMessage);

    document.querySelectorAll('.prompt-chip, .card-item').forEach(element => {
        element.addEventListener('click', () => {
            const query = element.getAttribute('data-query');
            if (query) {
                userInput.value = query;
                autoResizeTextarea();
                updateSendButtonState();
                handleSendMessage();
            }
        });
    });

    function autoResizeTextarea() {
        userInput.style.height = 'auto';
        userInput.style.height = Math.min(userInput.scrollHeight, 180) + 'px';
    }

    function handleSendMessage() {
        const rawQuery = userInput.value.trim();
        if (!rawQuery && stagedAttachments.length === 0) return;

        let queryToSend = rawQuery;
        if (activeQuotedExcerpt) {
            queryToSend = `> "${activeQuotedExcerpt}"\n\n${rawQuery}`;
            activeQuotedExcerpt = "";
            if (quoteReplyPreview) quoteReplyPreview.classList.add('hidden');
            if (quoteReplyText) quoteReplyText.textContent = "";
            if (userInput) userInput.placeholder = "Message XortLogix High Level Assistant...";
        }

        sendUserQuery(queryToSend);
    }

    function scrollToBottom() {
        if (chatContainer) {
            chatContainer.scrollTo({ top: chatContainer.scrollHeight, behavior: 'smooth' });
        }
    }

    async function sendUserQuery(query) {
        welcomeScreen.classList.add('hidden');

        // Copy active attachments for sending & rendering
        const attachmentsToSend = [...stagedAttachments];

        userInput.value = '';
        autoResizeTextarea();
        stagedAttachments = [];
        renderAttachmentsTray();
        sendBtn.disabled = true;

        // Append User Message to UI (with attachments)
        const userMsgEl = appendMessageToDOM('user', query, [], true, attachmentsToSend);

        // Position screen immediately starting at user's newly sent message
        if (userMsgEl) {
            setTimeout(() => {
                userMsgEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 30);
        }

        // Create Assistant Message Container with Thinking Indicator
        const msgWrapper = document.createElement('div');
        msgWrapper.className = 'message-wrapper assistant';
        msgWrapper.innerHTML = `
            <div class="assistant-avatar">⚡</div>
            <div class="assistant-body">
                <div class="markdown-content"><span class="generating-indicator"><span class="generating-dots"><span></span><span></span><span></span></span> Thinking...</span></div>
                <div class="message-actions hidden">
                    <button class="action-btn copy-btn" title="Copy response" type="button">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                        <span>Copy</span>
                    </button>
                </div>
            </div>
        `;
        messagesList.appendChild(msgWrapper);

        const contentEl = msgWrapper.querySelector('.markdown-content');
        const actionsEl = msgWrapper.querySelector('.message-actions');
        const copyBtn = msgWrapper.querySelector('.copy-btn');
        
        let targetText = '';
        let currentText = '';
        let sources = [];
        let isDoneStreaming = false;
        let animationTimer = null;

        // Smooth Word-by-Word Typewriter Engine (ChatGPT Cadence)
        function updateTypewriter() {
            if (currentText.length < targetText.length) {
                const remaining = targetText.length - currentText.length;
                let step = 1;
                if (remaining > 150) {
                    step = 10;
                } else if (remaining > 60) {
                    step = 5;
                } else if (remaining > 20) {
                    step = 3;
                } else {
                    step = 1;
                }

                currentText += targetText.slice(currentText.length, currentText.length + step);
                contentEl.innerHTML = renderMarkdown(currentText) + '<span class="typing-cursor"></span>';

                // Keep view readable: gently scroll if typing line extends past bottom
                const rect = msgWrapper.getBoundingClientRect();
                const containerRect = chatContainer.getBoundingClientRect();
                if (rect.bottom > containerRect.bottom - 30) {
                    chatContainer.scrollTop += 6;
                }
            } else if (isDoneStreaming) {
                if (animationTimer) {
                    clearInterval(animationTimer);
                    animationTimer = null;
                }
                
                // Final clean render without cursor
                contentEl.innerHTML = renderMarkdown(currentText || 'No response generated.');

                // Show copy button
                if (actionsEl) actionsEl.classList.remove('hidden');
                if (copyBtn) {
                    copyBtn.addEventListener('click', () => {
                        navigator.clipboard.writeText(cleanLatexArtifacts(currentText));
                        const btnSpan = copyBtn.querySelector('span');
                        if (btnSpan) btnSpan.textContent = 'Copied!';
                        setTimeout(() => { if (btnSpan) btnSpan.textContent = 'Copy'; }, 2000);
                    });
                }
            }
        }

        // Start typewriter tick loop (18ms)
        animationTimer = setInterval(updateTypewriter, 18);

        try {
            const response = await authFetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    query: query,
                    conversation_id: currentConversationId,
                    top_k: appSettings.topK,
                    attachments: attachmentsToSend
                })
            });

            if (!response.ok) {
                if (animationTimer) clearInterval(animationTimer);
                const errData = await response.json().catch(() => ({ detail: response.statusText }));
                contentEl.innerHTML = renderMarkdown(`⚠️ **Error (${response.status}):** ${errData.detail || 'Failed to generate answer. Please check your Gemini API key or login session.'}`);
                return;
            }

            const reader = response.body.getReader();
            const decoder = new TextDecoder('utf-8');
            let buffer = '';

            while (true) {
                const { done, value } = await reader.read();
                if (done) break;

                buffer += decoder.decode(value, { stream: true });
                const lines = buffer.split('\n\n');
                buffer = lines.pop(); // keep trailing incomplete chunk in buffer

                for (const line of lines) {
                    const trimmed = line.trim();
                    if (!trimmed.startsWith('data:')) continue;
                    const jsonStr = trimmed.replace(/^data:\s*/, '');
                    try {
                        const evt = JSON.parse(jsonStr);

                        if (evt.type === 'meta') {
                            currentConversationId = evt.conversation_id;
                            if (currentConversationId) {
                                localStorage.setItem('ghl_active_conv_id', currentConversationId);
                            }
                            if (activeChatTitle && evt.conversation_title) {
                                activeChatTitle.textContent = evt.conversation_title;
                            }
                            if (headerDeleteBtn) {
                                headerDeleteBtn.classList.remove('hidden');
                            }
                        } else if (evt.type === 'chunk') {
                            targetText += evt.text;
                        } else if (evt.type === 'sources') {
                            sources = evt.sources || [];
                        } else if (evt.type === 'done') {
                            if (evt.conversation_id) {
                                currentConversationId = evt.conversation_id;
                                localStorage.setItem('ghl_active_conv_id', currentConversationId);
                            }
                            if (activeChatTitle && evt.conversation_title) activeChatTitle.textContent = evt.conversation_title;
                            loadConversations();
                        } else if (evt.type === 'error') {
                            targetText += `\n\n⚠️ **Error:** ${evt.detail}`;
                        }
                    } catch (pErr) {
                        console.warn('SSE Parse warning:', pErr);
                    }
                }
            }

            isDoneStreaming = true;

        } catch (err) {
            if (animationTimer) clearInterval(animationTimer);
            contentEl.innerHTML = renderMarkdown(`❌ **Network Error:** Could not connect to server: ${err.message}`);
        } finally {
            updateSendButtonState();
        }
    }

    // Append Message to UI (ChatGPT 1:1 Design with Attachments Support)
    function appendMessageToDOM(role, content, sources = [], animate = true, attachments = []) {
        const msgWrapper = document.createElement('div');
        msgWrapper.className = `message-wrapper ${role}`;

        if (role === 'user') {
            let attachmentsHtml = '';
            if (attachments && attachments.length > 0) {
                attachmentsHtml = '<div class="bubble-attachments-wrap">';
                attachments.forEach((att) => {
                    if (att.type === 'image' && att.data) {
                        attachmentsHtml += `<img src="${att.data}" class="bubble-img-thumb" alt="${escapeHtml(att.name)}" title="Click to enlarge">`;
                    } else if (att.type === 'audio' && att.data) {
                        attachmentsHtml += `
                            <div class="bubble-audio-player">
                                <span class="bubble-audio-label">🎙️ ${escapeHtml(att.name)}</span>
                                <audio controls src="${att.data}"></audio>
                            </div>
                        `;
                    } else {
                        attachmentsHtml += `
                            <div class="bubble-file-chip">
                                <span>📄</span>
                                <span>${escapeHtml(att.name)}</span>
                            </div>
                        `;
                    }
                });
                attachmentsHtml += '</div>';
            }

            let textHtml = '';
            if (content) {
                if (content.startsWith('> "') || content.startsWith('>')) {
                    textHtml = `<div class="user-bubble-text markdown-content">${renderMarkdown(content)}</div>`;
                } else {
                    textHtml = `<div class="user-bubble-text">${escapeHtml(content)}</div>`;
                }
            }

            msgWrapper.innerHTML = `
                <div class="user-bubble">
                    ${attachmentsHtml}
                    ${textHtml}
                </div>
            `;

            // Attach image click listener for Lightbox
            msgWrapper.querySelectorAll('.bubble-img-thumb').forEach(img => {
                img.addEventListener('click', () => {
                    openImageLightbox(img.src);
                });
            });

        } else {
            const htmlContent = renderMarkdown(content);

            msgWrapper.innerHTML = `
                <div class="assistant-avatar">⚡</div>
                <div class="assistant-body">
                    <div class="markdown-content">${htmlContent}</div>
                    <div class="message-actions">
                        <button class="action-btn copy-btn" title="Copy response" type="button">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                            <span>Copy</span>
                        </button>
                    </div>
                </div>
            `;
        }

        messagesList.appendChild(msgWrapper);

        // Interactive Handlers for Assistant Messages
        if (role === 'assistant') {
            const copyBtn = msgWrapper.querySelector('.copy-btn');
            if (copyBtn) {
                copyBtn.addEventListener('click', () => {
                    navigator.clipboard.writeText(cleanLatexArtifacts(content));
                    const btnSpan = copyBtn.querySelector('span');
                    if (btnSpan) btnSpan.textContent = 'Copied!';
                    setTimeout(() => { if (btnSpan) btnSpan.textContent = 'Copy'; }, 2000);
                });
            }
        }

        return msgWrapper;
    }

    function scrollToBottom() {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function escapeHtml(text) {
        if (!text) return '';
        return text
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    
    

    
    // Admin Logic
    const adminLogoutBtn = document.getElementById('admin-logout-btn');
    const adminTable = document.getElementById('admin-users-table-body');
    const showAddFormBtn = document.getElementById('admin-add-user-btn');
    const addModal = document.getElementById('admin-add-user-modal');
    const closeAddModalBtn = document.getElementById('close-admin-add-modal');
    const saveUserBtn = document.getElementById('admin-save-user-btn');
    const cancelAddBtn = document.getElementById('admin-cancel-add-btn');
    const adminError = document.getElementById('admin-error-alert');
    const searchInput = document.getElementById('admin-search-input');
    
    let allUsersData = [];

    if (adminLogoutBtn) {
        adminLogoutBtn.addEventListener('click', async () => {
            try {
                await authFetch('/api/auth/logout', { method: 'POST' });
            } catch (e) {}
            localStorage.removeItem('ghl_session_token');
            currentUser = null;
            document.getElementById('admin-view').classList.add('hidden');
            showAuthView();
        });
        
        const closeAdminModal = () => {
            addModal.classList.add('hidden');
            adminError.classList.add('hidden');
            document.getElementById('new-user-name').value = '';
            document.getElementById('new-user-email').value = '';
            document.getElementById('new-user-pwd').value = '';
        };

        showAddFormBtn.addEventListener('click', () => addModal.classList.remove('hidden'));
        closeAddModalBtn.addEventListener('click', closeAdminModal);
        cancelAddBtn.addEventListener('click', closeAdminModal);
        
        saveUserBtn.addEventListener('click', async () => {
            adminError.classList.add('hidden');
            const name = document.getElementById('new-user-name').value;
            const email = document.getElementById('new-user-email').value;
            const pwd = document.getElementById('new-user-pwd').value;
            
            if(!name || !email || !pwd) {
                adminError.textContent = "All fields are required.";
                adminError.classList.remove('hidden');
                return;
            }
            
            // simple loading state on button
            saveUserBtn.textContent = 'Creating...';
            saveUserBtn.disabled = true;

            const res = await authFetch('/api/admin/users', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name: name, email: email, password: pwd })
            });
            
            saveUserBtn.textContent = 'Create Account';
            saveUserBtn.disabled = false;

            if (res.ok) {
                closeAdminModal();
                loadAdminUsers();
            } else {
                const data = await res.json();
                adminError.textContent = data.detail || "Failed to create account.";
                adminError.classList.remove('hidden');
            }
        });
        
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            const filtered = allUsersData.filter(u => u.name.toLowerCase().includes(query) || u.email.toLowerCase().includes(query));
            renderAdminTable(filtered);
        });
    }

    async function loadAdminUsers() {
        const res = await authFetch('/api/admin/users');
        if (res.ok) {
            const data = await res.json();
            allUsersData = data.users;
            renderAdminTable(allUsersData);
        }
    }
    
    function renderAdminTable(users) {
        if (!adminTable) return;
        adminTable.innerHTML = '';
        
        if (users.length === 0) {
            adminTable.innerHTML = `
                <tr>
                    <td colspan="3" style="padding: 40px; text-align: center; color: var(--text-muted);">
                        No employees found matching your search.
                    </td>
                </tr>`;
            return;
        }

        users.forEach(u => {
            const tr = document.createElement('tr');
            tr.style.borderBottom = '1px solid var(--border-color)';
            tr.style.transition = 'background-color 0.2s';
            tr.onmouseover = () => tr.style.backgroundColor = 'rgba(255,255,255,0.02)';
            tr.onmouseout = () => tr.style.backgroundColor = 'transparent';

            const initial = u.name.charAt(0).toUpperCase();

            tr.innerHTML = `
                <td>
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, #10b981, #059669); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 14px; flex-shrink: 0;">
                            ${initial}
                        </div>
                        <div style="min-width: 0;">
                            <div style="font-weight: 500; color: var(--text-primary); font-size: 14px; margin-bottom: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${escapeHtml(u.name)}</div>
                            <div style="color: var(--text-secondary); font-size: 12.5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${escapeHtml(u.email)}</div>
                        </div>
                    </div>
                </td>
                <td style="text-align: center;">
                    <span style="background-color: rgba(16, 185, 129, 0.12); color: #10b981; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; border: 1px solid rgba(16, 185, 129, 0.25); white-space: nowrap;">
                        ${u.message_count} messages
                    </span>
                </td>
                <td style="text-align: right;">
                    <button class="icon-btn" onclick="deleteUser('${u.id}')" title="Delete User" style="color: #ef4444; width: 34px; height: 34px; display: inline-flex; align-items: center; justify-content: center; border-radius: 8px;">
                        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                    </button>
                </td>
            `;
            adminTable.appendChild(tr);
        });
    }
    
    window.deleteUser = async function(uid) {
        if(!confirm('Are you sure you want to delete this user and ALL their chat history? This cannot be undone.')) return;
        const res = await authFetch(`/api/admin/users/${uid}`, { method: 'DELETE' });
        if (res.ok) loadAdminUsers();
        else alert('Failed to delete user.');
    };

    // System Status
    async function fetchSystemStatus() {
        try {
            const res = await fetch('/api/status');
            if (res.ok) {
                const data = await res.json();
                if (chunksCountBadge) {
                    chunksCountBadge.textContent = `${data.total_chunks.toLocaleString()} Chunks`;
                }
            }
        } catch (e) {
            console.warn('System status fetch warning:', e);
        }
    }

    // Sidebar Management for Mobile & Desktop
    function openSidebar() {
        if (!sidebar) return;
        if (window.innerWidth <= 768) {
            sidebar.classList.add('open');
            if (sidebarOverlay) sidebarOverlay.classList.add('active');
        } else {
            sidebar.classList.remove('closed');
        }
    }

    function closeSidebar() {
        if (!sidebar) return;
        if (window.innerWidth <= 768) {
            sidebar.classList.remove('open');
            if (sidebarOverlay) sidebarOverlay.classList.remove('active');
        } else {
            sidebar.classList.add('closed');
        }
    }

    function toggleSidebar() {
        if (!sidebar) return;
        if (window.innerWidth <= 768) {
            if (sidebar.classList.contains('open')) {
                closeSidebar();
            } else {
                openSidebar();
            }
        } else {
            sidebar.classList.toggle('closed');
        }
    }

    if (sidebarCloseBtn) {
        sidebarCloseBtn.addEventListener('click', closeSidebar);
    }
    if (sidebarOpenBtn) {
        sidebarOpenBtn.addEventListener('click', toggleSidebar);
    }
    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', closeSidebar);
    }

    // Auto adjust on resize
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            if (sidebarOverlay) sidebarOverlay.classList.remove('active');
            if (sidebar) sidebar.classList.remove('open');
        }
    });
});
