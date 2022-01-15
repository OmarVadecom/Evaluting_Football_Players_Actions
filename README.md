# Evaluting_Football_Players_Actions
## - Data science project in football analytics with  Wyscout dataset.

### Part I:
1- Load, Preprocessing wyscout dataset <br>
2- Feature Engineering over players Actions <br> 
3- split dataset train, test over various competitions <br>
4- Apply and compare between different Machine Learning Algorithms <br>
5- Evalute predictions <br>
6- calculate players's ranks based on played mintues over matches <br>
7- build a dashboard contains <br>
    - Some statics for each competitions (total goals, total fouls, ...) <br>
    - Top ten players for each competition <br>

<strong>Technology Used : Python - Dash - Plotly - scikit-learn </strong>

### Part II:
1- working on another dataset contains all goals of liverpool club 2019 <br>
2- generate a 2 video with 2d map for each choosen goal from a select element <br>
      - one for regular goal <br>
      - second visualize exploited and available spaces for each player for both teams <br>

<strong>Note :</strong> this part is just a proof of concept that we can do it for any events available dataset or live matches <br>

<strong>Technology Used : Python - Matplotlib - Moviepy </strong>

### Part III:
- build a django application for above parts with a login feature <br>
- Deployment on server <br>

<strong> Technology Used : Django Web Framework - (Django-plotly-dash to render dashboards) - Heroku server </strong>


#### Our main notebook which contains : 
   -> download datasets, preprocessing, applying XGB model, tuning with randomizedSearch, check Feature Importance, applying another models(Optimized XGB, Logistic regression, random forest) --- <a href='https://github.com/omar1890/Evaluting_Football_Players_Actions/blob/main/django_dash/notebooks/main_notebook_for_vaep_model.ipynb'>View it</a>
  
