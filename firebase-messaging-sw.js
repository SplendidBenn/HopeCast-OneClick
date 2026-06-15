// firebase-messaging-sw.js
importScripts('https://www.gstatic.com/firebasejs/10.14.1/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.14.1/firebase-messaging-compat.js');

// Your Firebase config (same as in index.html)
firebase.initializeApp({
  apiKey: "AIzaSyBNFHcNTSw5i43wfP8WWezC_tI0aVT-KEE",
  authDomain: "hopecast-1click.firebaseapp.com",
  projectId: "hopecast-1click",
  storageBucket: "hopecast-1click.appspot.com",
  messagingSenderId: "984543296926",
  appId: "1:984543296926:web:b1d0845a37c20fe2e8aa8f"
});

const messaging = firebase.messaging();

// Optional: Handle background messages
messaging.onBackgroundMessage((payload) => {
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: '/icon.png' // optional: add an icon later
  };
  self.registration.showNotification(notificationTitle, notificationOptions);
});