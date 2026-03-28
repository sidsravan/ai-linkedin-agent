import json

def generate_post(news):
    top = news[0]

    post = f"""
🚀 {top['title']}

🔍 SUMMARY:
• {top['summary'][:120]}
• This update improves developer productivity

🧠 EXPLANATION:

1. Problem  
Developers often face complexity when building cloud solutions.

2. Solution  
Azure simplifies this with managed services and automation.

3. Simple Analogy  
Imagine using a ready-made template instead of building everything from scratch.

4. Real-World Example  
A DevOps engineer can now deploy pipelines faster with fewer manual steps.

📊 ARCHITECTURE:

User → Azure Service → Processing → Output

🚀 KEY TAKEAWAYS:
✔ Faster development  
✔ Less manual work  
✔ Beginner-friendly tools  

Let me know if you'd like a deeper walkthrough!

#Azure #AI #DevOps #Cloud #Microsoft
"""

    return post