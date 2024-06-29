<template>
  <div class="bg-card text-card-foreground p-6 rounded-lg max-w-4xl mx-auto">
    <h2 class="text-2xl font-bold mb-4">General Information</h2>
    <form id="userForm" class="space-y-6" @submit.prevent="submitForm">
      <div class="flex items-center space-x-4">
        <img class="w-16 h-16 rounded-full" :src="avatarPreview" alt="User avatar" />
        <div class="flex-1">
          <label class="block text-sm font-medium mb-1" for="avatar">Upload avatar</label>
          <input ref="avatar" type="file" id="avatar" name="avatar" @change="previewAvatar" class="block w-full text-sm text-muted-foreground border border-input rounded-lg cursor-pointer bg-background focus:outline-none" />
          <p class="mt-1 text-xs text-muted-foreground">SVG, PNG, JPG or GIF (MAX. 800x400px).</p>
          <button type="button" @click="uploadAvatar" class="bg-primary text-primary-foreground hover:bg-primary/80 p-2 rounded-lg mt-2">Upload Avatar</button>
        </div>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
        <div>
          <label class="block text-sm font-medium mb-1" for="firstName">First Name</label>
          <input v-model="formData.firstName" type="text" id="firstName" name="firstName" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="First Name" />
        </div>
        <div>
          <label class="block text-sm font-medium mb-1" for="lastName">Last Name</label>
          <input v-model="formData.lastName" type="text" id="lastName" name="lastName" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Last Name" />
        </div>
        <div>
          <label class="block text-sm font-medium mb-1" for="email2">Secondary Email</label>
          <input v-model="formData.secondaryEmail" type="email" id="email2" name="email2" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="name@company.com" />
        </div>
        <div>
          <label class="block text-sm font-medium mb-1" for="address1">Primary Address</label>
          <input v-model="formData.primaryAddress" type="text" id="address1" name="address1" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Operational" />
        </div>
        <div>
          <label class="block text-sm font-medium mb-1" for="address2">Secondary Address</label>
          <input v-model="formData.secondaryAddress" type="text" id="address2" name="address2" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Operational" />
        </div>
        <div>
          <label class="block text-sm font-medium mb-1" for="country">Country</label>
          <input v-model="formData.country" type="text" id="country" name="country" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="e.g React Native Developer" />
        </div>
        <div>
          <label class="block text-sm font-medium mb-1" for="state">State</label>
          <input v-model="formData.state" type="text" id="state" name="state" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Owner" />
        </div>
        <div>
          <label class="block text-sm font-medium mb-1" for="zip_code">Zip Code</label>
          <input v-model="formData.zipCode" type="text" id="zip_code" name="zip_code" class="block w-full text-sm border border-input rounded-lg p-2 bg-background text-foreground" placeholder="Choose account type" />
        </div>
      </div>
      <button type="submit" class="bg-primary text-primary-foreground hover:bg-primary/80 p-2 rounded-lg mt-4">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        firstName: '',
        lastName: '',
        secondaryEmail: '',
        primaryAddress: '',
        secondaryAddress: '',
        country: '',
        state: '',
        zipCode: ''
      },
      avatarPreview: 'https://placehold.co/64x64'
    };
  },
  methods: {
    previewAvatar(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = e => {
          this.avatarPreview = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
    uploadAvatar() {
      const formData = new FormData();
      formData.append('avatar', this.$refs.avatar.files[0]);

      fetch('http://127.0.0.1:8000/backend/users/avatar/', {
        method: 'POST',
        body: formData,
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('jwt')}`
        }
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },
    submitForm() {
      fetch('http://127.0.0.1:8000/backend/users/adduserinfo/', {
        method: 'POST',
        body: JSON.stringify(this.formData),
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('jwt')}`
        }
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }
  }
};
definePageMeta({
  layout: 'home'
})
</script>

<style scoped>
/* Add scoped styles as needed */
</style>
