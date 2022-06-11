from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from .models import Person, Cars
from .forms import carForm, personForm

# აქ მგონი გასაგებია პირველ გვერდს აბრუნბს 
def index(request):   
    return render(request, 'index.html')


def all(request): #ყველა მონაცემს personalis 
    persons = Person.objects.all().order_by('id')
    return render(request, 'objects.html', {'person':persons} )

def allcars(request): # ყველა მონაცემი მანქანების
    cars = Cars.objects.all().order_by('id')
    return render(request, 'cars.html', {'cars':cars} )


def detail(request, pk): #detalurad achvenesb yvelafers
    employeers = get_object_or_404(Person, pk=pk)    
    car = employeers.car.all()
    return render(request, 'detail.html', {
        "employeers":employeers,
        "car" : car,
    })

#for searching experience 
def search(request):
    if request.method =="POST":
        
        search = request.POST['search']
        #ლისტების შექნა და გაფილტვრა საძიებო სიტყვებით
        selfid = Person.objects.filter(selfid__contains=search)
        
        name = Person.objects.filter(name__contains=search)
        
        lastname = Person.objects.filter(lastname__contains=search)

        for i  in name:
            print(i.check_car)
       
        
        #ამ რაღაცებს გადაცემს api და მერე ჩვენ ვხედავთ ამას 
        return render(request, 'search.html', {
                "search":search,
                "posts":name, 
                "lastname":lastname, 
                "selfid":selfid,
            }) 
    else:
        return render(request, 'search.html',  {})


#adding from django forms cars and employeers:

def add_car(request):
    submitted = False
    if request.method == "POST":
        form = carForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-car?submitted=True')
    else: 
        form = carForm
        if 'submitted' in request.GET:
            submitted= True
    return render(request, 'create.html', {'form':form, 'submitted':submitted})
    

def add_person(request):
    submitt = False
    if request.method == "POST":
        forms = personForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('/add-person?submitt=True')
    else: 
        forms = personForm
        if 'submitt' in request.GET:
            submitt= True
    return render(request, 'createperson.html', {'forms':forms, 'submitt':submitt})


#update from django forms,  persond and cars

def update_person(request, pk):
    employeer =  get_object_or_404(Person, pk=pk)
    form = personForm(request.POST or None, instance=employeer )
    if form.is_valid():
        form.save()
        return redirect('employeers')
    return render(request, 'updateperson.html',{
        'employeer':employeer,
        'form':form,
    })
    
def update_car(request, pk):
    car =  get_object_or_404(Cars, pk=pk)
    form = carForm(request.POST or None, instance=car )
    if form.is_valid():
        form.save()
        return redirect('allcars')
    return render(request, 'updatecar.html',{
        'car':car,
        'form':form,
    })


#delete methods : for cars and for employeers

def deletecar(request, car_id):
   car = get_object_or_404(Cars, pk=car_id)
   car.delete()
   return redirect('allcars')


def deleteper(request, person_id):
   person = get_object_or_404(Person, pk=person_id)
   person.delete()
   return redirect('employeers')
