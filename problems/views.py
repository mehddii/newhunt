from django.shortcuts import render
from django.http import HttpResponse

problems = [
    {
        'id': 1,
        'title': 'Sum of Two Numbers',
        'problem_uva_id': 100,
        'acceptance': '45%',
        'difficulty': 'Easy',
        'solved': 12345
    },
    {
        'id': 2,
        'title': 'The 3n + 1 Problem',
        'problem_uva_id': 371,
        'acceptance': '62%',
        'difficulty': 'Medium',
        'solved': 8765
    },
    {
        'id': 3,
        'title': 'Minesweeper',
        'problem_uva_id': 10189,
        'acceptance': '78%',
        'difficulty': 'Easy',
        'solved': 15987
    },
    {
        'id': 4,
        'title': 'Stack of Boxes',
        'problem_uva_id': 103,
        'acceptance': '35%',
        'difficulty': 'Hard',
        'solved': 5432
    },
    {
        'id': 5,
        'title': 'Interpreter',
        'problem_uva_id': 10082,
        'acceptance': '55%',
        'difficulty': 'Medium',
        'solved': 9101
    },
    {
        'id': 1,
        'title': 'Sum of Two Numbers',
        'problem_uva_id': 100,
        'acceptance': '45%',
        'difficulty': 'Easy',
        'solved': 12345
    },
    {
        'id': 2,
        'title': 'The 3n + 1 Problem',
        'problem_uva_id': 371,
        'acceptance': '62%',
        'difficulty': 'Medium',
        'solved': 8765
    },
    {
        'id': 3,
        'title': 'Minesweeper',
        'problem_uva_id': 10189,
        'acceptance': '78%',
        'difficulty': 'Easy',
        'solved': 15987
    },
    {
        'id': 4,
        'title': 'Stack of Boxes',
        'problem_uva_id': 103,
        'acceptance': '35%',
        'difficulty': 'Hard',
        'solved': 5432
    },
    {
        'id': 5,
        'title': 'Interpreter',
        'problem_uva_id': 10082,
        'acceptance': '55%',
        'difficulty': 'Medium',
        'solved': 9101
    },
    {
        'id': 1,
        'title': 'Sum of Two Numbers',
        'problem_uva_id': 100,
        'acceptance': '45%',
        'difficulty': 'Easy',
        'solved': 12345
    },
    {
        'id': 2,
        'title': 'The 3n + 1 Problem',
        'problem_uva_id': 371,
        'acceptance': '62%',
        'difficulty': 'Medium',
        'solved': 8765
    },
    {
        'id': 3,
        'title': 'Minesweeper',
        'problem_uva_id': 10189,
        'acceptance': '78%',
        'difficulty': 'Easy',
        'solved': 15987
    },
    {
        'id': 4,
        'title': 'Stack of Boxes',
        'problem_uva_id': 103,
        'acceptance': '35%',
        'difficulty': 'Hard',
        'solved': 5432
    },
    {
        'id': 5,
        'title': 'Interpreter',
        'problem_uva_id': 10082,
        'acceptance': '55%',
        'difficulty': 'Medium',
        'solved': 9101
    },
    {
        'id': 1,
        'title': 'Sum of Two Numbers',
        'problem_uva_id': 100,
        'acceptance': '45%',
        'difficulty': 'Easy',
        'solved': 12345
    },
    {
        'id': 2,
        'title': 'The 3n + 1 Problem',
        'problem_uva_id': 371,
        'acceptance': '62%',
        'difficulty': 'Medium',
        'solved': 8765
    },
    {
        'id': 3,
        'title': 'Minesweeper',
        'problem_uva_id': 10189,
        'acceptance': '78%',
        'difficulty': 'Easy',
        'solved': 15987
    },
    {
        'id': 4,
        'title': 'Stack of Boxes',
        'problem_uva_id': 103,
        'acceptance': '35%',
        'difficulty': 'Hard',
        'solved': 5432
    },
    {
        'id': 5,
        'title': 'Interpreter',
        'problem_uva_id': 10082,
        'acceptance': '55%',
        'difficulty': 'Medium',
        'solved': 9101
    } 
]

def home(request):
    return render(request, 'problems/index.html')

def problem_set(request):
    return render(request, 'problems/problems.html', context={"problems": problems})

def problem(request, id):
    return HttpResponse(f"Problem with id: <{id}>")