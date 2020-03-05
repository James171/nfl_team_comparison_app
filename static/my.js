
// Implementing Chart.js to show disparity of pivotal stats b/t team 2 and team 1

		
		var color = Chart.helpers.color;
		var horizontalBarChartData = {
			labels: jlist1,
			datasets: [{
				label: 'Dataset 1',
				backgroundColor: "red",
				borderWidth: 1,
				data: jlist2
			}]

		};

		window.onload = function() {
			var ctx = document.getElementById('canvas').getContext('2d');
			window.myHorizontalBar = new Chart(ctx, {
				type: 'horizontalBar',
				data: horizontalBarChartData,
				options: {
					// Elements options apply to all of the options unless overridden in a dataset
					// In this case, we are setting the border of each horizontal bar to be 2px wide
					elements: {
						rectangle: {
							borderWidth: 2,
						}
					},
					scales: {
						yAxes: [{
							barPercentage: 1.5
						}]
					},
					responsive: true,
					legend: {
						position: 'right',
					},
					title: {
						display: true,
						text: 'Team Comparison Chart',
						fontSize: 20
					}
				}
			});

		};

		

		var colorNames = Object.keys(window.chartColors);

		document.getElementById('addDataset').addEventListener('click', function() {
			var colorName = colorNames[horizontalBarChartData.datasets.length % colorNames.length];
			var dsColor = window.chartColors[colorName];
			var newDataset = {
				label: 'Dataset ' + (horizontalBarChartData.datasets.length + 1),
				backgroundColor: color(dsColor).alpha(0.5).rgbString(),
				borderColor: dsColor,
				data: []
			};

			for (var index = 0; index < horizontalBarChartData.labels.length; ++index) {
				newDataset.data.push(randomScalingFactor());
			}

			horizontalBarChartData.datasets.push(newDataset);
			window.myHorizontalBar.update();
		});

		

		

		
	