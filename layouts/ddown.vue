<template>
    <div>
        <div id="dropdownMenu" class="hidden absolute right-0 mt-2 w-48 bg-white text-zinc-800 rounded-lg shadow-lg">
            <div class="p-4">
                <p class="font-bold">Neil Sims</p>
                <p class="text-sm text-zinc-600">name@flowbite.com</p>
            </div>
            <div class="border-t border-zinc-200"></div>
            <a href="#" class="block px-4 py-2 hover:bg-zinc-100">My profile</a>
            <a href="#" class="block px-4 py-2 hover:bg-zinc-100">Account settings</a>
            <a href="#" class="block px-4 py-2 hover:bg-zinc-100">My likes</a>
            <a href="#" class="block px-4 py-2 hover:bg-zinc-100">Collections</a>
            <a href="#" class="block px-4 py-2 hover:bg-zinc-100">Pro version</a>
            <div class="border-t border-zinc-200"></div>
            <a href="#" class="block px-4 py-2 hover:bg-zinc-100">Sign out</a>
        </div>
    </div>
</template>
<script setup>
import { onMounted } from 'vue';

onMounted(() => {
    const avatarButton = document.getElementById('avatarButton');
    const dropdownMenu = document.getElementById('dropdownMenu');

    if (avatarButton && dropdownMenu) {
        avatarButton.addEventListener('click', (event) => {
            event.stopPropagation();
            dropdownMenu.classList.toggle('hidden');
        });

        document.addEventListener('click', () => {
            dropdownMenu.classList.add('hidden');
        });
    } else {
        console.error('Elements not found');
    }
});
</script>