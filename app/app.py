from flask import Flask, render_template, request, jsonify,Response,send_file
from datetime import timedelta
from main import file_builder, pdf_merge, clean_files


app = Flask(__name__, template_folder="templates", static_folder="templates/static")


@app.route('/', methods=['GET', 'POST'])  # 首页路由
def index():
    return render_template('mainPage.html')


@app.route('/upload.do', methods=['GET', 'POST'])
def upload():
    try:
        request.files['file'].save("tmp/" + request.files['file'].filename)
    except:
        return jsonify({"success": False})
    return jsonify({"success": True})


@app.route('/transfer.do', methods=['GET', 'POST'])  # 文件转换方法
def transfer():
    try:
        file_name = "combined_PDF.pdf"
        file_list = request.get_json()["file_list"]
        pdfs = file_builder(file_list)
        pdf_merge(pdfs, file_name)
        response = send_file(file_name, as_attachment=True)
        return response
    except:
        return


@app.route('/clean.do', methods=['GET', 'POST'])  # 文件转换方法
def clean():
    clean_files()
    return "ok"


if __name__ == '__main__':
    # 自动重载模板文件
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    # 设置静态文件缓存过期时间
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    Flask.run(app)
