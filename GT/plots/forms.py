from django import forms

class dfs_input_form(forms.Form):
    dropdown_choices = [
        ('mapusa', 'Mapusa'),
        ('panaji', 'Panaji'),
        ('margao', 'Margao'),
        ('ponda', 'Ponda'),
    ]
    
    Start = forms.ChoiceField(
        choices=dropdown_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

class a_star_form(forms.Form):
    dropdown_choices_start = [
        ('mapusa', 'Mapusa'),
        ('panaji', 'Panaji'),
        ('margao', 'Margao'),
        ('ponda', 'Ponda'),
    ]
    
    Start = forms.ChoiceField(
        choices=dropdown_choices_start,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    dropdown_choices_end = [
        ('mapusa', 'Mapusa'),
        ('panaji', 'Panaji'),
        ('margao', 'Margao'),
        ('ponda', 'Ponda'),
    ]
    
    End = forms.ChoiceField(
        choices=dropdown_choices_end,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

class deg_centrality_form(forms.Form):
    dropdown_choices = [
        ('mapusa', 'Mapusa'),
        ('panaji', 'Panaji'),
        ('margao', 'Margao'),
        ('ponda', 'Ponda'),
    ]
    
    Node = forms.ChoiceField(
        choices=dropdown_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

class radial_form(forms.Form):
    dropdown_choices = [
        ('mapusa', 'Mapusa'),
        ('panaji', 'Panaji'),
        ('margao', 'Margao'),
        ('ponda', 'Ponda'),
    ]

    
    Start = forms.ChoiceField(
        choices=dropdown_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
    
    )

    radius_in_km = forms.DecimalField(
        label="Radius (in kilometers)",
        min_value=0.1,  # Set the minimum allowed value for the radius
        widget=forms.NumberInput(attrs={'type': 'number', 'step': '0.01'}),  # Use type="number" and specify the step for decimal places
    )