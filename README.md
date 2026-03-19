<h2 align="center">📊 Model Training Progress</h2>

<div align="center">

<svg width="160" height="160" viewBox="0 0 120 120">

  <!-- Background Circle -->
  <circle cx="60" cy="60" r="50"
    stroke="#e6e6e6"
    stroke-width="10"
    fill="none" />

  <!-- Progress Circle -->
  <circle cx="60" cy="60" r="50"
    stroke="#00ff99"
    stroke-width="10"
    fill="none"
    stroke-dasharray="314"
    stroke-dashoffset="78"
    stroke-linecap="round"
    transform="rotate(-90 60 60)">
    
    <animate attributeName="stroke-dashoffset"
      from="314" to="78"
      dur="2s"
      fill="freeze" />
  </circle>

  <!-- Text -->
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
    font-size="22" fill="#333">
    75%
  </text>

</svg>

<p><b>⚡ Model Training Completion: 75%</b></p>

</div>
