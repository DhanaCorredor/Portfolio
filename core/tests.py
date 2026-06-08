from django.test import TestCase
from django.urls import reverse


class RoutesTests(TestCase):
    """Las tres páginas públicas responden 200."""

    def test_index_ok(self):
        self.assertEqual(self.client.get(reverse('core:index')).status_code, 200)

    def test_cv_web_ok(self):
        self.assertEqual(self.client.get(reverse('core:cv_marketing')).status_code, 200)

    def test_cv_print_ok(self):
        self.assertEqual(self.client.get(reverse('core:cv_marketing_print')).status_code, 200)


class I18nTests(TestCase):
    """El español es el idioma por defecto (sin prefijo) y el inglés vive en /en/."""

    def test_default_language_is_spanish(self):
        res = self.client.get('/')
        self.assertContains(res, 'Stack y herramientas')

    def test_english_prefix(self):
        res = self.client.get('/en/')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Stack & tools')


class ContentRegressionTests(TestCase):
    """Guardas frente a errores ya corregidos para que no reaparezcan."""

    def test_booking_link_uses_valid_domain(self):
        res = self.client.get(reverse('core:index'))
        self.assertContains(res, 'cal.com/dhanacorredor')
        self.assertNotContains(res, 'cal.eu')

    def test_og_image_is_absolute(self):
        res = self.client.get(reverse('core:index'), secure=True)
        self.assertContains(res, 'property="og:image" content="https://')

    def test_english_level_not_overclaimed(self):
        """El nivel de inglés es B1; nunca 'Professional'/'working proficiency'."""
        for url in (reverse('core:index'), reverse('core:cv_marketing'),
                    reverse('core:cv_marketing_print')):
            body = self.client.get(url).content.decode('utf-8')
            self.assertNotIn('working proficiency', body)

    def test_experience_has_no_standalone_radio_role(self):
        res = self.client.get(reverse('core:index'))
        self.assertNotContains(res, 'Communications Manager')
