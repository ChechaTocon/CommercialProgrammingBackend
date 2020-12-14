from django.contrib.auth import get_user_model, get_user
from django.test import TestCase
from reviews.models import Review, Movie, Category

class ReviewModelTest(TestCase):    

    @classmethod    
    def setUpTestData(cls):
        category = Category.objects.create(name = 'Terror',color= '#ffffff')
        movie = Movie.objects.create(poster='', movieName='Los vengadores', description='entretenida', category=category)
        userSave = get_user_model()(username='juanjo', first_name='Juan Jose', last_name='Ordoñez')
        userSave.set_password('juanjo123')
        userSave.save()

        Review.objects.create(comment='Es muy buena la peli bro', ranking=4, movie=movie, user=userSave)
        pass

    def test_comment_label(self):
        data = Review.objects.get(id=1)
        field_label = data._meta.get_field('comment').verbose_name        
        self.assertEquals(field_label,'comment')
    
    def test_ranking_label(self):
        data = Review.objects.get(id=1)
        field_label = data._meta.get_field('ranking').verbose_name        
        self.assertEquals(field_label,'ranking')
    
    def test_comment_value(self):
        data = Review.objects.get(id=1)         
        self.assertEquals(data.comment,'Es muy buena la peli bro')
    
    def test_ranking_value(self):
        data = Review.objects.get(id=1)         
        self.assertEquals(data.ranking, 4)
    
    def test_related_movieName_value(self):
        data = Review.objects.get(id=1)         
        self.assertEquals(data.movie.movieName, 'Los vengadores')
    
    def test_related_username_value(self):
        data = Review.objects.get(id=1)         
        self.assertEquals(data.user.username, 'juanjo')
    

