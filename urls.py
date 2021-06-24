from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from eamena.views.resource import ResourceEditorView
from eamena.views.bulk_uploader import upload_spreadsheet, validate, convert, download_template
uuid_regex = settings.UUID_REGEX

#overriding from arches.app.resource import ResourceEditorView
#comment-out line 10 to switch view back to core Arches

urlpatterns = [
	url(r"^resource/(?P<resourceid>%s)$" % uuid_regex, ResourceEditorView.as_view(), name="resource_editor"),
	url(r"^bulk-upload/excel-upload$", upload_spreadsheet, name="bulk_upload"),
	url(r"^bulk-upload/validate$", validate, name="bulk_upload_validate"),
	url(r"^bulk-upload/convert$", convert, name="bulk_upload_convert"),
	url(r"^bulk-upload/templates/(?P<graphid>%s)\.xlsx$" % uuid_regex, download_template, name="download_template"),
    url(r'^', include('arches.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.SHOW_LANGUAGE_SWITCH is True:
    urlpatterns = i18n_patterns(*urlpatterns)
