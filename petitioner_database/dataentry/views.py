from django.shortcuts import render, redirect
from .utils import check_csv_errors, get_all_custom_models
from uploads.models import Upload
from django.conf import settings
from django.contrib import messages
from .tasks import import_data_task
from django.core.management import call_command
from .models import Petitioner
from django.shortcuts import render, get_object_or_404


def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        #model_name = request.POST.get('model_name')
        model_name = "Petitioner"       

        upload = Upload.objects.create(file=file_path, model_name=model_name)

        relative_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)
        
        file_path = base_url+relative_path

        try:
            check_csv_errors(file_path, model_name)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('dataentry:import_data')

        import_data_task.delay(file_path, model_name)

        messages.success(request, 'Your data is being imported, you will be notified once it is done.')
        return redirect('dataentry:import_data')
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models': custom_models,
        }
    return render(request, 'dataentry/importdata.html', context)

def data_entry_view(request):
  
    petitioner = None
    petitioners = Petitioner.objects.all()
    return render(request, 'dataentry/data_entry_view.html', {'petitioner': petitioner, 'petitioners': petitioners})

def detail(request, id):

    petitioner = get_object_or_404(Petitioner, id=id)
    return render(request, 'dataentry/detail.html', {'petitioner': petitioner})
