from django.core.management.base import BaseCommand, CommandError
from problems.models import  Problem
from math import floor

import requests
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = 'https://uhunt.onlinejudge.org/api/p/'
        try:
            self.stdout.write(
                self.style.HTTP_INFO('Downloading data...')
            )
            response = requests.get(url)
            response.raise_for_status()  
            data = response.json()

            for problem in data:
                print(int(problem[1]))
                problem_uva_id = int(problem[1])
                title = problem[2]
                acceptance = int(problem[18]) / (int(problem[7]) + int(problem[10]) + sum([int(problem[i]) for i in range(12, 18)])) * 100
                difficulty = 'Easy'
                if acceptance < 33:
                    difficulty = 'Hard'
                elif acceptance < 66:
                    difficulty = 'Medium'
                solved = int(problem[3])
                url = f'https://onlinejudge.org/external/{floor(problem_uva_id / 100)}/{problem_uva_id}.pdf'
                Problem(problem_uva_id=problem_uva_id, title=title, acceptance=acceptance, difficulty=difficulty, solved=solved, url=url).save()
            

            self.stdout.write(
                self.style.SUCCESS('Successfully downloaded data and saved it to the db')
            )

        except requests.exceptions.RequestException as e:
            self.stderr.write(
                self.style.ERROR(f"Error downloading data: {e}")
            )
        except Exception as e:
            self.stderr.write(
                self.style.ERROR(f"An unexpected error occurred: {e}")
            )