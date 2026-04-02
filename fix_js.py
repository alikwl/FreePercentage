import os

base_dir = r"E:\websites\freepercentage\tools"

tools_data = {
    "discount-calculator": {
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
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    split_parts = content.split('<script src="../../assets/script.js"></script>')
    if len(split_parts) > 1:
        extra_js = """
    function downloadPDF() {
      const result = document.getElementById('resultSentence').textContent;
      const tool = document.title.split(' -')[0];
      const blob = new Blob([`${tool}\\n\\nResult: ${result}\\n\\nCalculated at FreePercentage.com`], { type: 'text/plain' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'calculation-result.txt';
      a.click();
    }
"""
        js_code = f'\n    <script>{data["js"]}{extra_js}    </script>\n</body>\n</html>'
        
        new_content = split_parts[0] + '<script src="../../assets/script.js"></script>' + js_code
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed JS for {tool}")