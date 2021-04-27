<script>
    import Papa from 'papaparse';
  
    let datapoints = []
    Papa.parse("https://vda-lab.github.io/assets/iris.csv", {
      header: true,
      download: true,
      complete: function(results) {
        datapoints = results.data
      }
    })
    let selected_datapoint = undefined;
    let mouse_x, mouse_y;
  
    const rescale = function(x, domain_min, domain_max, range_min, range_max) {
        return ((range_max - range_min)*(x-domain_min))/(domain_max-domain_min) + range_min
    }

    const setMousePosition = function(event) {
      mouse_x = event.clientX;
      mouse_y = event.clientY;
    }
    const lineGenerator = function(d) {
        let sl = +d.sepal_length;
        let pl = +d.petal_length;
        let sw = +d.sepal_width;
        let pw = +d.petal_width
        return "M 25 " + (25-3*sl) +
                " L " + (25+3*pl) + " 25" +
                " L 25 " + (25+3*sw) +
                " L " + (25-3*pw) + " 25 Z"
    }
  </script>
  
  <style>
    svg {
        background-color: whitesmoke;
    }
    circle {
      fill: steelblue;
      fill-opacity: 0.5;
    }
    #tooltip {
      position: fixed;
      background-color: rgb(227, 227, 227);
    }
    line {
        stroke: black;
    }
  </style>
  
  <svg width=400 height=400>
    {#each datapoints as datapoint}
      <circle
        cx={rescale(datapoint.sepal_length,4.3,7.9,20,380)}
        cy={rescale(datapoint.sepal_width,2.0,4.4,20,380)}
        r=6
        on:mouseover={(event) => {selected_datapoint = datapoint; setMousePosition(event)}}
        on:mouseout={() => {selected_datapoint = undefined}}/>
    {/each}
  </svg>
  <br/>

  {#if selected_datapoint != undefined}
    <svg width=50 height=50
        id="tooltip"
        style="left: {mouse_x + 10}px; top: {mouse_y - 10}px">
    <line class="axis" x1=0 x2=50 y1=25 y2=25 />
    <line class="axis" x1=25 x2=25 y1=0 y2=50 />
    <path d={lineGenerator(selected_datapoint)} />
    <circle cx=25 cy=25 r=2 style="fill: white; fill-opacity: 1;" />
    </svg>
  {/if}