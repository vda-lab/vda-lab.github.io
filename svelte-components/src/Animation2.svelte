<script>
    let degree = 0;
    let dim = 200;
  
    $: theta = degree*Math.PI/180
    const x = function(r, theta) {
      return r*Math.cos(theta)
    }
    const y = function(r, theta) {
      return r*Math.sin(theta)
    }
  
    const interval = setInterval(() => {
      degree += 1;
      if ( degree == 360 ) {
        degree = 0
      }
    }, 10);
  </script>
  
  <style>
    line {
      stroke: black;
    }
    circle {
      stroke: black;
      fill: none;
    }
  </style>
  
  {degree}<br/>
  <svg width={dim+10} height={dim+10}>
    <g transform="translate({dim/2+5},{dim/2+5})">
      <circle cx=0 cy=0 r={dim/2} />
      <line x1=0 y1=0 x2={x(dim/2, theta)} y2={y(dim/2, theta)} />
    </g>
  </svg>