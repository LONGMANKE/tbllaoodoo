{
    'name': 'Bookstore Theme',
    'description': 'Books, Magazines, Music',
    'category': 'Theme/Retail',
    'summary': 'Library, Books, Magazines, Literature, Musics, Media, Store',
    'sequence': 250,
    'version': '2.1.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_cta_box.xml',
        'views/snippets/s_striped_top.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_cards_grid.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_sidegrid.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_card_offset.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_image_title.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_images_mosaic.xml',
        'views/snippets/s_showcase.xml',
        'views/snippets/s_freegrid.xml',
        'views/snippets/s_features_wall.xml',
        'views/snippets/s_image_punchy.xml',
        'views/snippets/s_empowerment.xml',
        'views/snippets/s_masonry_block.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_features_grid.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_quotes_carousel_minimal.xml',
        'views/snippets/s_unveil.xml',
        'views/snippets/s_quadrant.xml',
        'views/snippets/s_numbers_showcase.xml',
        'views/snippets/s_key_benefits.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_carousel_intro.xml',
        'views/snippets/s_pricelist_boxed.xml',
        'views/snippets/s_image_hexagonal.xml',
        'views/snippets/s_striped_center_top.xml',
        'views/snippets/s_intro_pill.xml',
        'views/snippets/s_big_number.xml',
        'views/snippets/s_image_frame.xml',
        'views/snippets/s_wavy_grid.xml',
        'views/snippets/s_shape_image.xml',
        'views/snippets/s_images_constellation.xml',
        'views/snippets/s_text_cover.xml',
        'views/snippets/s_accordion.xml',
        'views/snippets/s_accordion_image.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/bookstore_description.jpg',
        'static/description/bookstore_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_product_list_default_image_1': '/theme_bookstore/static/src/img/snippets/s_product_1.jpg',
        'website.s_image_text_default_image': '/theme_bookstore/static/src/img/snippets/s_image_text.jpg',
        'website.library_image_02': '/theme_bookstore/static/src/img/snippets/library_image_02.jpg',
        'website.s_cover_default_image': '/theme_bookstore/static/src/img/snippets/s_cover.jpg',
        'website.s_media_list_default_image_1': '/theme_bookstore/static/src/img/snippets/s_media_list_1.jpg',
        'website.s_media_list_default_image_2': '/theme_bookstore/static/src/img/snippets/s_media_list_2.jpg',
        'website.s_text_image_default_image': '/theme_bookstore/static/src/img/snippets/s_text_image.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_banner', 's_key_images', 's_title', 's_accordion_image', 's_cta_box'],
    },
    'new_page_templates': {
        'about': {
            'personal': ['s_text_cover', 's_image_text', 's_text_block_h2', 's_numbers', 's_features', 's_call_to_action'],
        },
        'landing': {
            '1': ['s_banner', 's_features', 's_masonry_block', 's_call_to_action', 's_references', 's_quotes_carousel'],
            '2': ['s_cover', 's_text_image', 's_text_block_h2', 's_three_columns_landing_1', 's_call_to_action'],
            '3': ['s_text_cover', 's_text_block_h2', 's_three_columns', 's_showcase', 's_color_blocks_2', 's_quotes_carousel', 's_call_to_action'],
        },
        'services': {
            '2': ['s_text_cover', 's_image_text', 's_text_image', 's_image_text_2nd', 's_call_to_action'],
        },
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-bookstore.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_bookstore/static/src/js/tour.js',
        ],
    }
}