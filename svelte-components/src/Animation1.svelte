<script>
    let counter = 0;
  
    const interval = setInterval(() => {
      counter += 1;
      if ( counter > 400 ) {
        counter = 0
      }
    }, 100)
  </script>
  
  <style>
    rect {
      fill: steelblue;
    }
  </style>
  
  {counter}<br/>
  <svg width=400 height=50>
    <rect x={counter} y=15 width=20 height=20 />
  </svg>