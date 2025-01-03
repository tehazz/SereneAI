document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById('mentalHealthChart').getContext('2d');
    const data = {
        labels: [
            'Students reporting anxiety (16.5%)', 
            'Students with depression (12.3%)', 
            'Students with suicidal thoughts (13.1%)'
        ],
        datasets: [{
            label: 'Percentage',
            data: [16.5, 12.3, 13.1],
            backgroundColor: [
                'rgba(121, 134, 203, 0.5)',  // Blue for Anxiety
                'rgba(183, 83, 102, 0.5)',   // Red for Depression
                'rgba(183, 121, 158, 0.5)'   // Purple for Suicidal Thoughts
            ],
            borderColor: [
                'rgba(121, 134, 203, 1)',    // Blue border for Anxiety
                'rgba(183, 83, 102, 1)',     // Red border for Depression
                'rgba(183, 121, 158, 1)'     // Purple border for Suicidal Thoughts
            ],
            borderWidth: 1
        }]
    };

    const config = {
        type: 'bar',
        data: data,
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    color: '#F3E8FF'
                },
                x: {
                    color: '#F3E8FF'
                }
            }
        }
    };

    new Chart(ctx, config);
});

