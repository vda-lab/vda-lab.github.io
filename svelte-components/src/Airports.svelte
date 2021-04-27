<script>
    let slider_value = 5000;
  
    let datapoints = []
    fetch("https://vda-lab.github.io/assets/svelte-flights.json")
      .then(res => res.json())
      .then(data => datapoints = data.slice(1,5000))
  
    const rescale = function(x, domain_min, domain_max, range_min, range_max) {
      return ((range_max - range_min)*(x-domain_min))/(domain_max-domain_min) + range_min
    }
  </script>
  
  <style>
    circle {
      opacity: 0.5;
      fill: blue;
    }
    circle.international {
      fill: red;
    }
    circle.hidden {
      opacity: 0.05;
    }
  </style>
  
  <h1>Airport flights data</h1>
  Airports serving flights in this range (km): {slider_value - 1000} - {slider_value + 1000} <br/>
  <input type="range" min="1" max="15406" bind:value={slider_value} class="slider" id="myRange" />
  <svg width=1000 height=500>
    {#each datapoints as datapoint}
      <circle cx={rescale(datapoint.from_long, -180, 180, 0, 800)}
              cy={rescale(datapoint.from_lat, -90, 90, 400, 0)}
              r={rescale(datapoint.distance, 1, 15406, 2,10)}
              class:international="{datapoint.from_country != datapoint.to_country}"
              class:hidden="{Math.abs(datapoint.distance - slider_value) > 1000}">
        <title>{datapoint.from_airport}</title>
      </circle>
    {/each}
  </svg>