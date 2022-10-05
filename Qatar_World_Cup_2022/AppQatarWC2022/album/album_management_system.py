from AppQatarWC2022.album.album import Album, AlbumPage
from AppQatarWC2022.countries.country import Country


class AlbumManagementSystem:
      
    def __init__(self):
        self.album = None
       
    def refresh_album_with(self,generated_sticker_collection):
    
        qualified_countries = Country.objects.filter(qualified = True)
        
        album_page_collection = []

        for country in qualified_countries:
            stickers_filtered_by_country = next((generated_sticker for generated_sticker in generated_sticker_collection if generated_sticker.country() == country),[])
            album_page = AlbumPage.composed_of(country,country.background(),stickers_filtered_by_country)
            album_page.initialize_slots()
            album_page_collection.append(album_page)

        self.update_album_with(Album.composed_of(album_page_collection,album_page))

    def update_album_with(self,album):
        self.album = album

    def name(self):
        return 'Sistema de Administración de Álbum'