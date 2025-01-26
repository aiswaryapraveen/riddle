from django.shortcuts import render
from django.http import JsonResponse
import random
import time

# List of random paragraphs for testing
PARAGRAPHS = [
    "Technology has revolutionized the way we communicate and access information. With the advent of smartphones and the internet, people can connect with others instantly, regardless of their location. Social media platforms have become a significant part of daily life, providing a space to share ideas and experiences. However, excessive use of technology can lead to issues such as reduced face-to-face interactions and digital addiction. It is important to find a healthy balance and use technology responsibly.",
    "Nature has an incredible ability to inspire and heal. Spending time outdoors, surrounded by trees, mountains, or the ocean, can have a calming effect on the mind. Studies have shown that being in nature reduces stress, enhances creativity, and boosts mental health. Activities like hiking, gardening, or simply walking in a park allow individuals to reconnect with the natural world. Embracing nature is not just beneficial for personal well-being but also fosters a sense of responsibility to protect the environment.",
    "The concept of time management is crucial in achieving success in any field. By organizing tasks and prioritizing activities, individuals can ensure that their time is spent efficiently. Many people struggle with procrastination, which can lead to stress and missed opportunities. Developing a structured plan and setting clear goals can help overcome these challenges. Effective time management not only boosts productivity but also improves overall well-being, as it allows for a balance between work and leisure.",
]

def start(request):
    # Select a random paragraph
    paragraph = random.choice(PARAGRAPHS)
    request.session['paragraph'] = paragraph
    request.session['start_time'] = time.time()  # Record start time
    return render(request, 'type/start.html', {'paragraph': paragraph})

def tsubmit(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        paragraph = request.session.get('paragraph', '')
        start_time = request.session.get('start_time', 0)
        end_time = time.time()

        # Calculate time taken
        time_taken = end_time - start_time
        words_per_minute = len(user_input.split()) / (time_taken / 60)

        # Calculate accuracy
        correct_chars = sum(1 for a, b in zip(user_input, paragraph) if a == b)
        accuracy = (correct_chars / len(paragraph)) * 100 if paragraph else 0

        # Return results
        return JsonResponse({
            'time_taken': round(time_taken, 2),
            'wpm': round(words_per_minute, 2),
            'accuracy': round(accuracy, 2),
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
