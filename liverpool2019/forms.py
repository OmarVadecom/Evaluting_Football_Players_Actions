from django import forms
  
# iterable
GEEKS_CHOICES =(
     ('Liverpool [3] - 0 Bournemouth','Liverpool [3] - 0 Bournemouth'),
     ('Bayern 0 - [1] Liverpool','Bayern 0 - [1] Liverpool'),
     ('Fulham 0 - [1] Liverpool','Fulham 0 - [1] Liverpool'), 
     ('Southampton 1 - [2] Liverpool','Southampton 1 - [2] Liverpool'),
     ('Liverpool [2] - 0 Porto','Liverpool [2] - 0 Porto'), 
     ('Porto 0 - [2] Liverpool','Porto 0 - [2] Liverpool'),
     ('Liverpool [4] - 0 Barcelona','Liverpool [4] - 0 Barcelona'), 
     ('Liverpool [1] - 0 Wolves','Liverpool [1] - 0 Wolves'),
     ('Liverpool [3] - 0 Norwich','Liverpool [3] - 0 Norwich'), 
     ('Liverpool [2] - 1 Chelsea','Liverpool [2] - 1 Chelsea'),
     ('Liverpool [2] - 1 Newcastle','Liverpool [2] - 1 Newcastle'), 
     ('Liverpool [2] - 0 Salzburg','Liverpool [2] - 0 Salzburg'),
     ('Genk 0 - [3] Liverpool','Genk 0 - [3] Liverpool'), 
     ('Liverpool [2] - 0 Man City','Liverpool [2] - 0 Man City'),
     ('Liverpool [1] - 0 Everton','Liverpool [1] - 0 Everton'), 
     ('Liverpool [2] - 0 Everton','Liverpool [2] - 0 Everton'),
     ('Bournemouth 0 - 3 Liverpool','Bournemouth 0 - 3 Liverpool'), 
     ('Liverpool [1] - 0 Watford','Liverpool [1] - 0 Watford'),
     ('Leicester 0 - [3] Liverpool','Leicester 0 - [3] Liverpool')
)
  
# creating a form 
class ChooseMatch(forms.Form):
     choose_match = forms.ChoiceField(choices = GEEKS_CHOICES)