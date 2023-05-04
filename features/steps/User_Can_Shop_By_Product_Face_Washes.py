from behave import given, when, then


@given ("Open the main page")
def open_cureskin_page (context):
     context.app.main_page.open_main_url()
     context.app.main_page.remove_popup_banner()


@then ("Click on 'Shop by product' - select Face Washes")
def click_shop_by_product (context):
     context.app.header.shopping_by_product()
     context.app.header.face_washes()


@when ("Verify {expected_result} 'Face Wash' results is shown")
def verify_search_results (context, expected_result):
     context.app.search_results.verifying_search_result(expected_result)

