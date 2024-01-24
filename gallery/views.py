import os
import json
from typing import Any
from unittest.mock import patch
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

PROJECT_ROOT = os.path.dirname(__file__);
def list(request):
	html = "<html><body>Will be a list here</body></html>"
	files = os.listdir(".\gallery/photos");
	print("files: ");
	print(files);
	data = json.dumps(files);
	print("serizialize: ");
	print(data);
	return HttpResponse(data, status=200, content_type="application/json");

def get_photos(path):
    if path != None:
        photo_folder = path
    else:
        photo_folder = os.path.join(PROJECT_ROOT, 'static/photos');
    print("folders:");
    print(photo_folder);
    files = os.listdir(photo_folder);
    files.sort();
    return files

def get_subgalleries():
	photo_folder = os.path.join(PROJECT_ROOT, 'static/photos');
	galleries = [ f.path for f in os.scandir(photo_folder) if f.is_dir() ]
	print("galleries:");
	print(galleries);
	return galleries;

    
class GalleryView(View):
	def __init__(self):
		print("init GalleryView");
#	def get_files():
#			print("get_files");
#			files = get_photos(None);
#			return files;
	# subgallery
	def get(self, request, path_num):
		print("subgallery GET\n");
		print("path:", path_num);
		subs = get_subgalleries();
		path = subs[path_num];
		files = get_photos(path);
		print("files: ", files);
		list = [];
		print("path: ", path);

		for name in files:
			fullname = path + '\\' + name;
			print("fullname: ", fullname);
			list.append(fullname);
			print("list: ");
			print(list);
		return render(request, "gallery1.html", {"list": list, "sub": path_num });

class PhotoView(View):
	def __init__(self, **kwargs: Any):
		print("PhotoView init");
		super().__init__(**kwargs)
		def get(self, request):
			print("PhotoView GET");
			name = request.GET.get('name');
			print("photo mame:");
			print(name);
			return render(request, "photo.html", {"name": name});
def showPhoto(request, num, sub):
	print("showPhoto: ")
	print(num);
	pathes = get_subgalleries();
	
	path = pathes[sub];
	print("photo path: ", path);
	
	files = get_photos(path);
	name = path + '\\' + files[num];
	return render(request, "Photo.html", {"name": name, "sub" : sub});

def subgalleriesView(request):
	list = get_subgalleries();
	sublist = [];
	print("list:", list);
	for dir in list:
		name = os.path.basename(dir);
		print("name: ", name);
		sublist.append({"dirname": name, "path": dir  })
	
	return render(request, "SubGalleries.html", {"list": sublist });



