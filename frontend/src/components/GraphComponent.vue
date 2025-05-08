<template>
    <v-card class="ma-4">
      <v-card-title>Maintenance Predictions</v-card-title>
      <v-card-text>
        <canvas id="predictionChart"></canvas>
      </v-card-text>
    </v-card>
  </template>
  
  <script>
  import { Line } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale } from 'chart.js'
  
  ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale)
  
  export default {
    name: 'GraphComponent',
    extends: Line,
    props: ['predictions'],
    mounted() {
      this.renderChart({
        labels: this.predictions.map(p => p.equipment_id),
        datasets: [
          {
            label: 'Failure Probability',
            data: this.predictions.map(p => p.failure_probability * 100),
            borderColor: 'rgba(75, 192, 192, 1)',
            fill: false
          }
        ]
      }, {
        responsive: true,
        plugins: {
          title: { display: true, text: 'Equipment Failure Probability' }
        }
      })
    }
  }
  </script>