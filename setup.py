from setuptools import setup, find_packages

setup(
    name="authorizer_demo",  # パッケージ名
    version="0.1",  # バージョン番号
    packages=find_packages(),  # どのパッケージを含めるかを自動で探す
    install_requires=[  # 依存関係（インストール時に必要なライブラリ）
        "numpy",  # 例: numpy を依存パッケージとして指定
        "requests",
    ],
    author="SWX-HASHIMOTO",  # 作者名
    author_email="shingo.hashimoto@serverworks.co.jp",  # 作者のメールアドレス
    description="This project-demo for Lambda authorizer",  # プロジェクトの簡単な説明
    long_description=open("README.md").read(),  # 詳細な説明（通常はREADMEファイル）
    long_description_content_type="text/markdown",  # READMEの形式（markdownなど）
    url="https://github.com/SWX-HASHIMOTO/authorizer_demo.git",  # プロジェクトのURL
)
