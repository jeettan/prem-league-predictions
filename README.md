# Premier League Prediction Project

A machine learning project to predict Premier League match results using team statistics and match history.

## Team Statistics

Source: [Statto – Team Statistics](https://statto.pythonanywhere.com/stats/teams?sort=team&dir=asc&limit=all)

## Match Results (2025–2026 Season)

Match results are collected using the scraping script in `scrape.py`.

## Model

Uses XGBoost to predict three possible outcomes:

- Home Win
- Draw
- Home Loss

## Training data

Training data is based on 2025-2026 season of prem league

## Improvements

More datais needed to increase the accuracy of predictions
