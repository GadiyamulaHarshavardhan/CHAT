import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import MediaFile

UPLOAD_DIR = settings.MEDIA_ROOT / "uploads"


@csrf_exempt
def chunk_upload(request):
    """
    Handles large uploads using chunks:
    - "file" uploaded in request.FILES
    - "filename" in POST
    - "chunk_index"
    - "total_chunks"
    """

    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    file = request.FILES.get("file")
    filename = request.POST.get("filename")
    chunk = int(request.POST.get("chunk_index"))
    total = int(request.POST.get("total_chunks"))

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    temp_path = UPLOAD_DIR / f"{filename}.part"

    # Append chunk to temp file
    with open(temp_path, "ab") as f:
        for chunk_part in file.chunks():
            f.write(chunk_part)

    # Final assembly
    if chunk + 1 == total:
        final_path = UPLOAD_DIR / filename
        os.rename(temp_path, final_path)

        return JsonResponse({"completed": True, "file_url": f"/media/uploads/{filename}"})

    return JsonResponse({"chunk_received": chunk})



@csrf_exempt
def upload_media(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid"}, status=400)

    file = request.FILES["file"]
    media_type = request.POST.get("media_type", "file")

    media = MediaFile.objects.create(
        file=file,
        media_type=media_type
    )

    return JsonResponse({
        "url": media.file.url,
        "id": media.id,
        "media_type": media.media_type
    })
