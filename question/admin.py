from django.contrib import admin

from .models import *

class CoreJavaAdmin(admin.ModelAdmin):
	list_display = ['id','cjq', 'timestamp', 'updated']
	list_display_links = ['cjq']
	class Meta:
		model = CoreJava

class BasicJavaAdmin(admin.ModelAdmin):
	list_display = ['id','bjq', 'timestamp', 'updated']
	list_display_links = ['bjq']
	class Meta:
		model = CoreJava

class AdvancedJavaAdmin(admin.ModelAdmin):
	list_display = ['id','ajq', 'timestamp', 'updated']
	list_display_links = ['ajq']
	class Meta:
		model = AdvancedJava

class CProgAdmin(admin.ModelAdmin):
	list_display = ['id','cpq', 'timestamp', 'updated']
	list_display_links = ['cpq']
	class Meta:
		model = CProg


class DataStructureAdmin(admin.ModelAdmin):
	list_display = ['id','dsq', 'timestamp', 'updated']
	list_display_links = ['dsq']
	class Meta:
		model = DataStructure

class DbmsAdmin(admin.ModelAdmin):
	list_display = ['id','dbq', 'timestamp', 'updated']
	list_display_links = ['dbq']
	class Meta:
		model = Dbms


class ComputerNetworkAdmin(admin.ModelAdmin):
	list_display = ['id','cnq', 'timestamp', 'updated']
	list_display_links = ['cnq']
	class Meta:
		model = ComputerNetwork


class OperatingSystemAdmin(admin.ModelAdmin):
	list_display = ['id','osq', 'timestamp', 'updated']
	list_display_links = ['osq']
	class Meta:
		model = OperatingSystem


class UnixAdmin(admin.ModelAdmin):
	list_display = ['id','uxq', 'timestamp', 'updated']
	list_display_links = ['uxq']
	class Meta:
		model = Unix

class CommentAdmin(admin.ModelAdmin):
	list_display = ['id','email', 'timestamp', 'updated']
	list_display_links = ['email']
	class Meta:
		model = Comment


admin.site.register(CoreJava, CoreJavaAdmin)

admin.site.register(BasicJava, BasicJavaAdmin)

admin.site.register(AdvancedJava, AdvancedJavaAdmin)

admin.site.register(CProg, CProgAdmin)

admin.site.register(DataStructure, DataStructureAdmin)

admin.site.register(Dbms, DbmsAdmin)

admin.site.register(ComputerNetwork, ComputerNetworkAdmin)

admin.site.register(OperatingSystem, OperatingSystemAdmin)

admin.site.register(Unix, UnixAdmin)

admin.site.register(Comment, CommentAdmin)