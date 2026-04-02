import os

base_dir = r"E:\websites\freepercentage\tools"

tools_data = {
    "discount-calculator": {
        "html": """
          <h2>Discount Calculator — Free Tool</h2>
          <div class="calc-input-group">
            <label for="p1">Original Price ($)</label>
            <input type="number" id="p1" placeholder="e.g. 500">
          </div>
          <div class="calc-input-group">
            <label for="p2">Discount Percentage (%)</label>
            <input type="number" id="p2" placeholder="e.g. 20">
          </div>
          <button class="btn btn-primary" onclick="calculate()">Calculate Discount</button>

          <div class="result-display" id="result" style="display:none;">
            <div class="result-number" id="resultValue"></div>
            <div class="result-sentence" id="resultSentence"></div>
            <div class="result-actions">
              <button onclick="copyResult()">📋 Copy Result</button>
              <button onclick="downloadPDF()">📄 Download PDF</button>
            </div>
          </div>
          <div class="chart-container" id="chartArea" style="display:none;">
            <canvas id="resultChart" width="300" height="300"></canvas>
          </div>
""",
        "js": """
    let chartInstance = null;
    function drawPieChart(value1, value2, labels) {
      const ctx = document.getElementById('resultChart').getContext('2d');
      if (chartInstance) chartInstance.destroy();
      document.getElementById('chartArea').style.display = 'block';
      chartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: labels,
          datasets: [{ data: [value1, value2], backgroundColor: ['#0056b3', '#ff6b00'], borderWidth: 0, hoverOffset: 8 }]
        },
        options: { responsive: true, plugins: { legend: { position: 'bottom' } } }
      });
    }

    function calculate() {
      const p1 = parseFloat(document.getElementById('p1').value);
      const p2 = parseFloat(document.getElementById('p2').value);

      if (isNaN(p1) || isNaN(p2)) {
        alert('Please enter valid numbers.');
        return;
      }

      const discountAmt = (p1 * (p2 / 100));
      const finalPrice = p1 - discountAmt;

      document.getElementById('resultValue').textContent = '$' + finalPrice.toLocaleString(undefined, {maximumFractionDigits: 2});
      document.getElementById('resultSentence').textContent = `You save $${discountAmt.toLocaleString(undefined, {maximumFractionDigits: 2})}. The final checkout price is $${finalPrice.toLocaleString(undefined, {maximumFractionDigits: 2})}.`;

      drawPieChart(finalPrice, discountAmt, ['Final Price', 'Amount Saved']);
      document.getElementById('result').style.display = 'block';
    }
"""
    },
    
    "percentage-increase-decrease": {
        "html": """
          <h2>% Increase/Decrease Calculator</h2>
          <div class="calc-input-group">
            <label for="p1">Initial Value</label>
            <input type="number" id="p1" placeholder="e.g. 100">
          </div>
          <div class="calc-input-group">
            <label for="p2">Final Value</label>
            <input type="number" id="p2" placeholder="e.g. 150">
          </div>
          <button class="btn btn-primary" onclick="calculate()">Calculate Change</button>

          <div class="result-display" id="result" style="display:none;">
            <div class="result-number" id="resultValue"></div>
            <div class="result-sentence" id="resultSentence"></div>
            <div class="result-actions">
              <button onclick="copyResult()">📋 Copy Result</button>
              <button onclick="downloadPDF()">📄 Download PDF</button>
            </div>
          </div>
""",
        "js": """
    function calculate() {
      const p1 = parseFloat(document.getElementById('p1').value);
      const p2 = parseFloat(document.getElementById('p2').value);

      if (isNaN(p1) || isNaN(p2) || p1 === 0) {
        alert('Please enter valid numbers. Initial value cannot be zero.');
        return;
      }

      const diff = p2 - p1;
      const pct = (diff / p1) * 100;
      const changeType = pct >= 0 ? "Increase" : "Decrease";

      document.getElementById('resultValue').textContent = Math.abs(pct).toLocaleString(undefined, {maximumFractionDigits: 4}) + '% ' + changeType;
      document.getElementById('resultSentence').textContent = `The change from ${p1} to ${p2} is a ${Math.abs(pct).toLocaleString(undefined, {maximumFractionDigits: 4})}% ${changeType.toLowerCase()}. The absolute difference is ${Math.abs(diff).toLocaleString(undefined, {maximumFractionDigits: 4})}.`;

      document.getElementById('result').style.display = 'block';
    }
"""
    },
    
    "percentage-difference": {
        "html": """
          <h2>Percentage Difference Calculator</h2>
          <div class="calc-input-group">
            <label for="p1">Value A</label>
            <input type="number" id="p1" placeholder="e.g. 40">
          </div>
          <div class="calc-input-group">
            <label for="p2">Value B</label>
            <input type="number" id="p2" placeholder="e.g. 50">
          </div>
          <button class="btn btn-primary" onclick="calculate()">Calculate Difference</button>

          <div class="result-display" id="result" style="display:none;">
            <div class="result-number" id="resultValue"></div>
            <div class="result-sentence" id="resultSentence"></div>
            <div class="result-actions">
              <button onclick="copyResult()">📋 Copy Result</button>
              <button onclick="downloadPDF()">📄 Download PDF</button>
            </div>
          </div>
""",
        "js": """
    function calculate() {
      const p1 = parseFloat(document.getElementById('p1').value);
      const p2 = parseFloat(document.getElementById('p2').value);

      if (isNaN(p1) || isNaN(p2)) {
        alert('Please enter valid numbers.');
        return;
      }
      if (p1 === 0 && p2 === 0) {
        alert('Both values cannot be exactly zero.');
        return;
      }

      const diff = Math.abs(p1 - p2);
      const avg = (p1 + p2) / 2;
      const pct = (diff / Math.abs(avg)) * 100;

      document.getElementById('resultValue').textContent = pct.toLocaleString(undefined, {maximumFractionDigits: 4}) + '% Difference';
      document.getElementById('resultSentence').textContent = `The absolute percentage difference between ${p1} and ${p2} is ${pct.toLocaleString(undefined, {maximumFractionDigits: 4})}%. The average of the two values is ${avg}.`;

      document.getElementById('result').style.display = 'block';
    }
"""
    },
    
    "reverse-percentage": {
        "html": """
          <h2>Reverse Percentage Calculator</h2>
          <div class="calc-input-group">
            <label for="p1">Final Value</label>
            <input type="number" id="p1" placeholder="e.g. 120">
          </div>
          <div class="calc-input-group">
            <label for="p2">Percentage Applied (%)</label>
            <input type="number" id="p2" placeholder="e.g. 20">
          </div>
          <div class="calc-input-group" style="display: flex; flex-direction: column;">
            <label for="type">Operation Type</label>
            <select id="type" style="padding: 10px; width: 100%; border: 1px solid var(--border); border-radius: var(--radius); font-size: 1rem; background: var(--white); color: var(--text);">
                <option value="increase">This was an Increase (Added)</option>
                <option value="decrease">This was a Decrease (Subtracted)</option>
            </select>
          </div>
          <button class="btn btn-primary" onclick="calculate()">Find Original Value</button>

          <div class="result-display" id="result" style="display:none;">
            <div class="result-number" id="resultValue"></div>
            <div class="result-sentence" id="resultSentence"></div>
            <div class="result-actions">
              <button onclick="copyResult()">📋 Copy Result</button>
              <button onclick="downloadPDF()">📄 Download PDF</button>
            </div>
          </div>
""",
        "js": """
    function calculate() {
      const p1 = parseFloat(document.getElementById('p1').value);
      const p2 = parseFloat(document.getElementById('p2').value);
      const type = document.getElementById('type').value;

      if (isNaN(p1) || isNaN(p2)) {
        alert('Please enter valid numbers.');
        return;
      }

      let originalValue;
      if (type === 'increase') {
         originalValue = p1 / (1 + (p2 / 100));
      } else {
         if (p2 >= 100) {
             alert('Decrease percentage cannot be 100% or more for a non-zero final value.');
             return;
         }
         originalValue = p1 / (1 - (p2 / 100));
      }

      document.getElementById('resultValue').textContent = originalValue.toLocaleString(undefined, {maximumFractionDigits: 4});
      
      const wording = type === 'increase' ? 'added to' : 'subtracted from';
      document.getElementById('resultSentence').textContent = `Before the ${p2}% was ${wording} the original value, the original value was exactly ${originalValue.toLocaleString(undefined, {maximumFractionDigits: 4})}.`;

      document.getElementById('result').style.display = 'block';
    }
"""
    },
    
    "percentage-of-percentage": {
        "html": """
          <h2>% of a Percentage Calculator</h2>
          <div class="calc-input-group">
            <label for="p1">First Percentage (%)</label>
            <input type="number" id="p1" placeholder="e.g. 10">
          </div>
          <div class="calc-input-group">
            <label for="p2">Second Percentage (%)</label>
            <input type="number" id="p2" placeholder="e.g. 50">
          </div>
          <button class="btn btn-primary" onclick="calculate()">Calculate</button>

          <div class="result-display" id="result" style="display:none;">
            <div class="result-number" id="resultValue"></div>
            <div class="result-sentence" id="resultSentence"></div>
            <div class="result-actions">
              <button onclick="copyResult()">📋 Copy Result</button>
              <button onclick="downloadPDF()">📄 Download PDF</button>
            </div>
          </div>
""",
        "js": """
    function calculate() {
      const p1 = parseFloat(document.getElementById('p1').value);
      const p2 = parseFloat(document.getElementById('p2').value);

      if (isNaN(p1) || isNaN(p2)) {
        alert('Please enter valid numbers.');
        return;
      }

      const pct = (p1 / 100) * (p2 / 100) * 100;

      document.getElementById('resultValue').textContent = pct.toLocaleString(undefined, {maximumFractionDigits: 6}) + '%';
      document.getElementById('resultSentence').textContent = `${p1}% of ${p2}% evaluates to exactly ${pct.toLocaleString(undefined, {maximumFractionDigits: 6})}%.`;

      document.getElementById('result').style.display = 'block';
    }
"""
    },
    
    "salary-increment": {
        "html": """
          <h2>Salary Increment Calculator</h2>
          <div class="calc-input-group">
            <label for="p1">Current Salary</label>
            <input type="number" id="p1" placeholder="e.g. 50000">
          </div>
          <div class="calc-input-group">
            <label for="p2">Increment Percentage (%)</label>
            <input type="number" id="p2" placeholder="e.g. 15">
          </div>
          <button class="btn btn-primary" onclick="calculate()">Calculate New Salary</button>

          <div class="result-display" id="result" style="display:none;">
            <div class="result-number" id="resultValue"></div>
            <div class="result-sentence" id="resultSentence"></div>
            <div class="result-actions">
              <button onclick="copyResult()">📋 Copy Result</button>
              <button onclick="downloadPDF()">📄 Download PDF</button>
            </div>
          </div>
          <div class="chart-container" id="chartArea" style="display:none;">
            <canvas id="resultChart" width="300" height="300"></canvas>
          </div>
""",
        "js": """
    let chartInstance = null;
    function drawPieChart(value1, value2, labels) {
      const ctx = document.getElementById('resultChart').getContext('2d');
      if (chartInstance) chartInstance.destroy();
      document.getElementById('chartArea').style.display = 'block';
      chartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: labels,
          datasets: [{ data: [value1, value2], backgroundColor: ['#0056b3', '#28a745'], borderWidth: 0, hoverOffset: 8 }]
        },
        options: { responsive: true, plugins: { legend: { position: 'bottom' } } }
      });
    }

    function calculate() {
      const p1 = parseFloat(document.getElementById('p1').value);
      const p2 = parseFloat(document.getElementById('p2').value);

      if (isNaN(p1) || isNaN(p2)) {
        alert('Please enter valid numbers.');
        return;
      }

      const incrementAmt = p1 * (p2 / 100);
      const newSalary = p1 + incrementAmt;

      document.getElementById('resultValue').textContent = newSalary.toLocaleString(undefined, {maximumFractionDigits: 2});
      document.getElementById('resultSentence').textContent = `Congratulations! A ${p2}% hike gives you an increment of ${incrementAmt.toLocaleString(undefined, {maximumFractionDigits: 2})}. Your new total salary will be ${newSalary.toLocaleString(undefined, {maximumFractionDigits: 2})}.`;

      drawPieChart(p1, incrementAmt, ['Base Salary', 'Increment Amount']);
      document.getElementById('result').style.display = 'block';
    }
"""
    }
}

for tool, data in tools_data.items():
    filepath = os.path.join(base_dir, tool, "index.html")
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the <section id="calculator"> inner contents
    calc_start = content.find('<section id="calculator" class="calculator-card">')
    if calc_start != -1:
        calc_end = content.find('</section>', calc_start)
        if calc_end != -1:
            new_section = '<section id="calculator" class="calculator-card">\n' + data['html'] + '\n        </section>'
            content = content[:calc_start] + new_section + content[calc_end+10:]
            
    # Add JS at the bottom right before </body>
    if 'function calculate()' not in content:
        # Common functions
        extra_js = "\n    function downloadPDF() {\n      const result = document.getElementById('resultSentence').textContent;\n      const tool = document.title.split(' -')[0];\n      const blob = new Blob([`${tool}\\n\\nResult: ${result}\\n\\nCalculated at FreePercentage.com`], { type: 'text/plain' });\n      const a = document.createElement('a');\n      a.href = URL.createObjectURL(blob);\n      a.download = 'calculation-result.txt';\n      a.click();\n    }\n"
        js_block = f'<script>{data["js"]}{extra_js}  </script>\n</body>'
        content = content.replace('</body>', js_block)
    
    # Add Chart.js to head if needed
    if 'Chart.js' not in content and 'chartInstance' in data['js']:
        content = content.replace('</head>', '  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>\n</head>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated logic for {tool}")
