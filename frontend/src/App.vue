<template>
    <v-app>
      <v-app-bar app color="primary" dark>
        <v-toolbar-title>Predictive Maintenance Simulator</v-toolbar-title>
      </v-app-bar>
      <v-main>
        <v-container>
          <UploadComponent @data-loaded="handleDataLoaded" />
          <GraphComponent :predictions="predictions" v-if="predictions.length" />
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  import UploadComponent from './components/UploadComponent.vue'
  import GraphComponent from './components/GraphComponent.vue'
  
  export default {
    name: 'App',
    components: {
      UploadComponent,
      GraphComponent
    },
    data() {
      return {
        predictions: []
      }
    },
    methods: {
      handleDataLoaded(data) {
        this.predictions = data.predictions
      }
    }
  }
  </script>