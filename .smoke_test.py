from streamlit.testing.v1 import AppTest
app = AppTest.from_file('app.py', default_timeout=30).run()
assert not app.exception, app.exception
for page in ['My story', 'Projects', 'Skills', 'Say hello', 'Overview']:
    app.sidebar.radio[0].set_value(page).run()
    assert not app.exception, (page, app.exception)
app.sidebar.radio[0].set_value('Projects').run()
app.text_input[0].set_value('no-such-project').run()
assert any('No projects match' in item.value for item in app.info)
app.text_input[0].set_value('Python').run()
assert len(app.subheader) == 2
app.sidebar.radio[0].set_value('Say hello').run()
app.button[0].click().run()
assert app.error
app.text_input[0].set_value('Visitor')
app.text_area[0].set_value('Nice portfolio')
app.checkbox[0].check()
app.button[0].click().run()
assert app.success and not app.exception
app.button[1].click().run()
assert 'feedback' not in app.session_state
print('PASS: five pages, filters, form validation, session submission and clearing')
