from wtforms import Form 
from wtforms import StringField, PasswordField,EmailField,BooleanField,SubmitField,IntegerField,SelectField, SelectMultipleField, RadioField, widgets
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula",{
        validators.DataRequired(message='El campo es requerido')
    })
    nombre=StringField("Nombre",[
        validators.DataRequired(message='El campo es requerido')
    ])
    apellido=StringField("Apellido",{
        validators.DataRequired(message='El campo es requerido')
    })
    correo=EmailField("Correo",[
        validators.Email(message='Ingrese Correo valido')
    ])



class pizzaForm(Form):
    nombre = StringField("Nombre del Cliente", [
        validators.DataRequired(message="El nombre es requerido")
    ])

    direccion = StringField("Dirección", [
        validators.DataRequired(message="La dirección es requerida")
    ])

    telefono = StringField("Teléfono", [
        validators.DataRequired(message="El teléfono es requerido")
    ])

    tamannio = RadioField("Tamaño de pizza", choices=[
        ("Chica", "Chica"),
        ("Mediana", "Mediana"),
        ("Grande", "Grande")
    ], validators=[validators.DataRequired(message="Selecciona un tamaño")])

    ingredientes = SelectMultipleField("Ingredientes Extras ($10 c/u)",
        choices=[
            ("Queso", "Queso Extra"), 
            ("Pepperoni", "Pepperoni"), 
            ("Jamón", "Jamón"), 
            ("Piña", "Piña")
        ],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
    )

    num_pizzas = IntegerField("Número de Pizzas", [
        validators.DataRequired(message="Debes indicar cuántas pizzas"),
        validators.NumberRange(min=1, max=50, message="Debe ser entre 1 y 50 pizzas")
    ], default=1)




