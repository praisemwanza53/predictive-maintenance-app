<template>
    <v-card class="ma-4">
      <v-card-title>Upload Equipment Data</v-card-title>
      <v-card-text>
        <v-file-input
          label="Upload Excel File"
          accept=".xlsx,.xls"
          @change="handleFileUpload"
          :loading="loading"
        ></v-file-input>
      </v-card-text>
    </v-card>
  </template>
  
  <script>
  export default {
    name: 'UploadComponent',
    data() {
      return {
        loading: false
      }
    },
    methods: {
      async handleFileUpload(file) {
        if (!file) return
        this.loading = true
        const formData = new FormData()
        formData.append('file', file)
        
        try {
          const response = await fetch('http://localhost:8000/upload', {
            method: 'POST',
            body: formData
          })
          const data = await response.json()
          this.$emit('data-loaded', data)
        } catch (error) {
          console.error('Upload failed:', error)
        } finally {
          this.loading = false
        }
      }
    }
  }
  </script>