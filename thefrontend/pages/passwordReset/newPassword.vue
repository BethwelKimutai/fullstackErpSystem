<template>
    <body class="font-mono bg-gray-400">
        <!-- Container -->
        <div class="container mx-auto">
            <div class="flex justify-center px-6 my-12">
                <!-- Row -->
                <div class="w-full xl:w-3/4 lg:w-11/12 flex">
                    <!-- Col -->
                    <div class="w-full h-auto bg-gray-400 hidden lg:block lg:w-1/2 bg-cover rounded-l-lg"
                        style="background-image: url('https://source.unsplash.com/oWTW-jNGl9I/600x800')"></div>
                    <!-- Col -->
                    <div class="w-full lg:w-1/2 bg-white p-5 rounded-lg lg:rounded-l-none">
                        <div class="px-8 mb-4 text-center">
                            <h3 class="pt-4 mb-2 text-2xl">Forgot Your Password?</h3>
                            <p class="mb-4 text-sm text-gray-700">
                                We get it, stuff happens. Just enter your username below and we'll send you a
                                link to reset your password!
                            </p>
                        </div>
                        <form class="px-8 pt-6 pb-8 mb-4 bg-white rounded" @submit.prevent="resetPassword">
                            <div class="mb-4">
                                <label class="block mb-2 text-sm font-bold text-gray-700" for="username">
                                    Username or Email
                                </label>
                                <input
                                    v-model="usernameOrEmail"
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="usernameOrEmail" type="text" placeholder="Enter username or email..." />
                            </div>
                            <div class="mb-4">
                                <label class="block mb-2 text-sm font-bold text-gray-700" for="newPassword">
                                    New Password
                                </label>
                                <input
                                    v-model="newPassword"
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="newPassword" type="password" placeholder="Enter new password..." />
                            </div>
                            <div class="mb-4">
                                <label class="block mb-2 text-sm font-bold text-gray-700" for="confirmPassword">
                                    Confirm New Password
                                </label>
                                <input
                                    v-model="confirmPassword"
                                    class="w-full px-3 py-2 text-sm leading-tight text-gray-700 border rounded shadow appearance-none focus:outline-none focus:shadow-outline"
                                    id="confirmPassword" type="password" placeholder="Enter confirmation password..." />
                            </div>
                            <div class="mb-6 text-center">
                                -Your password should be at least 12 characters long.
                                -Use a combination of uppercase letters, lowercase letters, numbers, and special characters (e.g., !, @, #, $, %, ^, &, *).
                                -Do not include easily accessible personal information such as your name, birthday, phone number, or address.
                            </div>
                            <div class="mb-6 text-center">
                                <button
                                    class="w-full px-4 py-2 font-bold text-white bg-red-500 rounded-full hover:bg-red-700 focus:outline-none focus:shadow-outline"
                                    type="submit">
                                    Reset Password
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </body>
</template>

<script>
export default {
    data() {
        return {
            usernameOrEmail: '',
            newPassword: '',
            confirmPassword: ''
        };
    },
    methods: {
        async resetPassword() {
            // Simple front-end validation
            if (!this.usernameOrEmail || !this.newPassword || !this.confirmPassword) {
                alert('All fields are required.');
                return;
            }
            if (this.newPassword !== this.confirmPassword) {
                alert('Passwords do not match.');
                return;
            }

            try {
                const response = await fetch('http://127.0.0.1:8000/backend/users/newpassword/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: this.usernameOrEmail,
                        new_password: this.newPassword,
                        confirm_password: this.confirmPassword
                    })
                });

                const result = await response.json();

                if (response.ok) {
                    alert('Password updated successfully.');
                    await this.$router.push('/');

                } else {
                    alert(result.message || 'Error updating password.');
                }
            } catch (error) {
                alert('An error occurred: ' + error.message);
            }
        }
    }
};
</script>
