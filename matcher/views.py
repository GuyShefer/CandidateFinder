from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Candidate, Job
from .serializers import CandidateSerializer
from django.db.models import Count, Q


@api_view(['GET'])
def candidate_finder(request, job_id):

    try:
        job = Job.objects.all().get(id=job_id)
    except Job.DoesNotExist:
        return Response('Job not found, Please try another ID', 404)

    job_title = job.title
    job_required_skills = [skill.name for skill in job.skills.all()]

    try:
        candiates_filterd = Candidate.objects.filter(Q(title__icontains=job_title)).filter(
            skills__name__in=job_required_skills).annotate(total=Count('id')).order_by('-total').prefetch_related('skills')
    except Candidate.DoesNotExist:
        return Response('No suitable candidates were found for the job', 404)

    response = {
        'Job title': job_title,
        'Required skills': job_required_skills,
        'Candidates': CandidateSerializer(list(candiates_filterd), many=True).data
    }

    return Response(response)
