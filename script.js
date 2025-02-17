const currentWeightDisplay = document.getElementById('currentWeight');
const averageWeightDisplay = document.getElementById('averageWeight');
const overloadStatusDisplay = document.getElementById('overloadStatus');
const alertList = document.getElementById('alertList');
const ctx = document.getElementById('weightChart').getContext('2d');

let weightData = [];
let chart;

// Chart.js setup
chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [], // Time labels (you'll add these)
    datasets: [{
      label: 'Weight',
      data: weightData,
      borderColor: 'blue',
      borderWidth: 1,
      fill: false
    }]
  },
  options: { /* ...Chart.js options for scales, tooltips, etc. */ }
});



// Example data update (replace with your actual data source)
function updateWeightData(weight) {
    weightData.push(weight);
    chart.data.datasets[0].data = weightData;
    chart.update();

    currentWeightDisplay.textContent = `${weight} kg`;
    // Calculate and display average weight (you'll need to store recent readings)

    // Overload detection (example)
    if (weight > 10000) { // Example threshold
      overloadStatusDisplay.textContent = "OVERLOAD!";
      overloadStatusDisplay.classList.add("overload-alert");
      addAlert("Truck Overload Detected!");
    } else {
      overloadStatusDisplay.textContent = "Normal";
      overloadStatusDisplay.classList.remove("overload-alert");
    }
}


function addAlert(message) {
  const newAlert = document.createElement('li');
  newAlert.textContent = message;
  newAlert.classList.add("overload-alert"); // Add class if needed
  alertList.appendChild(newAlert);
}



// Example: Simulate incoming data (replace with your actual data source)
setInterval(() => {
  const randomWeight = Math.floor(Math.random() * 12000); // Simulate weight data
  updateWeightData(randomWeight);
}, 2000); // Update every 2 seconds