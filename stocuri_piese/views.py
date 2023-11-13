from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.http import HttpResponse
from .forms import CautaPiesaForm, CautaModelForm
import json

# Create your views here.

def base(request):
    return render(request, "base.html")

def cautare_piesa_veche(request):
    form = CautaPiesaForm()
    return render(request, "cautare_piesa_veche.html", {"form":form})

def cautare_model(request):
    form = CautaModelForm()
    return render (request, "cautare_modele.html", {"form":form})


def cauta_piesa_veche(request):
    model_input = request.GET.get("model_input")
    rezultate = []
    if model_input:
        with connection.cursor() as cursor:
            model_exists = (f"""
            SELECT nume_model
            FROM modele_coduri_piese
            WHERE nume_model = '{model_input}'
            """)
            cursor.execute(model_exists)
            model_exists = cursor.fetchone()

            if not model_exists:
                return render (request, "rezultate_cauta_piesa_veche.html", {"model_inexistent": True, "model_input": model_input})
            
            sql_query =(f"""
                SELECT DISTINCT modele_coduri_piese.cod_piesa, stocuri.denumire_piesa, stocuri.document_date
                FROM modele_coduri_piese
                LEFT JOIN coduri_piese ON modele_coduri_piese.cod_piesa = coduri_piese.cod_piesa
                LEFT JOIN stocuri ON coduri_piese.cod_piesa = stocuri.cod_piesa
                WHERE modele_coduri_piese.nume_model = '{model_input}'
                    AND stocuri.document_date IS NOT NULL
                ORDER BY stocuri.document_date
            """)

            cursor.execute(sql_query)
            rezultate = cursor.fetchall()
            print(rezultate)

    return render (request, "rezultate_cauta_piesa_veche.html", {"rezultate": rezultate, "model_input": model_input})

            

def cauta_model_dupa_cod_piesa(request):
    cod_piesa_input = request.GET.get("cod_piesa_input", None)
    rezultate =[]
    if cod_piesa_input:
        with connection.cursor() as cursor:
            sql_query = (f"""
                SELECT nume_model
                FROM modele_coduri_piese
                WHERE cod_piesa = '{cod_piesa_input}'         
            """)
            cursor.execute(sql_query)
            rezultate_db = cursor.fetchall()
            print(rezultate_db)
            
        
        rezultate = [{"model": row[0]} for row in rezultate_db]
   
    
    return render (request, "rezultate_modele.html", {"rezultate": rezultate, "cod_piesa_input": cod_piesa_input})


