from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
import os


class Command(BaseCommand):
    help = 'Add Google OAuth app to the database'

    def add_arguments(self, parser):
        parser.add_argument('--secret', type=str, help='Google OAuth Client Secret')

    def handle(self, *args, **options):
        # Google OAuth credentials
        provider = 'google'
        name = 'Google Login'
        client_id = '1086375766165-hgv5meqlr0qv83ca9iptcph6lcqgbk2q.apps.googleusercontent.com'
        
        # Get secret from command argument, environment variable, or prompt user
        secret = options.get('secret')
        if not secret:
            secret = os.getenv('GOOGLE_CLIENT_SECRET')
        if not secret:
            secret = input('Enter your Google Client Secret: ')
        
        # Check if Google app already exists
        if SocialApp.objects.filter(provider=provider).exists():
            self.stdout.write(self.style.WARNING('Google OAuth app already exists'))
            return
        
        # Create the Google SocialApp
        app = SocialApp.objects.create(
            provider=provider,
            name=name,
            client_id=client_id,
            secret=secret,
        )
        
        # Add or get sites
        # Local site
        site1, created = Site.objects.get_or_create(
            id=1,
            defaults={'domain': '127.0.0.1:8000', 'name': '127.0.0.1:8000'}
        )
        if created:
            self.stdout.write(f'Created Site: {site1.domain}')
        app.sites.add(site1)
        
        # Production site
        site2, created = Site.objects.get_or_create(
            id=2,
            defaults={'domain': 'jonzfaj.pythonanywhere.com', 'name': 'PSUSphere'}
        )
        if created:
            self.stdout.write(f'Created Site: {site2.domain}')
        app.sites.add(site2)
        
        self.stdout.write(self.style.SUCCESS('✅ Google OAuth app added successfully!'))
        self.stdout.write(f'Provider: {provider}')
        self.stdout.write(f'Client ID: {client_id}')
        self.stdout.write('Sites: 127.0.0.1:8000, jonzfaj.pythonanywhere.com')
