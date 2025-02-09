######  Research on rice leaf pest and disease detection (code)
RGC-YOLO
###
A rice leaf pest detection method is introduced to address the problems of low detection precision, slow detection speed, limited recognized species, and high model complexity, based on the improved YOLOv8s (You Only Look Once) model, in this paper. The model is based on YOLOv8s as its base model, incorporating a Re-parameterized Convolution Ghost Cross Stage Partial Efficient Layer Aggregation Networks (RGCSPELAN) structure, where the RGCSPELAN structure replaces the C2F module. In addition, RT-DETR incorporates an aittention-based internal feature interaction (AIFI) structure, which replaces the spatial pyramid pooling fast layer from YOLOv8, resulting in the model becoming more focused on high-level feature images. The model is based on YOLOv8s and integrates a Re-parameterized Convolution Ghost Cross Stage Partial Efficient Layer Aggregation Networks (RGCSPELAN) structure, replacing the C2F module. Additionally, RT-DETR incorporates an attention-based internal feature interaction (AIFI) structure, which replaces the spatial pyramid pooling fast layer from YOLOv8. This modification enhances the model's focus on high-level feature images. The Adaptive Downsampling (ADown) structure in YOLOv9 is introduced to capture higher-level image features by reducing the spatial dimension of the feature map. Meanwhile, the Context Anchor Attention (CAA) mechanism is introduced after the ADown network layer to enhance the features in the central region through global average pooling and one-dimensional bar convolution. Finally, the Task Align Dynamic Detection Head (TADDH) is introduced, which obtains joint features by achieving interactive alignment of otherwise independent classification and localization branching tasks. The model's ability to recognize small targets, as well as its detection and classification performance, is enhanced through the optimization of the model structure. The experimental results on the rice public dataset demonstrate that, compared to YOLOv8s, the improved model proposed in this paper has achieved increases of 1.1%, 1.1%, 0.4%, and 3% respectively in precision, recall, mAP@0.5 (calculates the mean average precision when IoU=0.5.), and mAP@0.5:0.95(calculates the mean average precision over multiple IoU thresholds from 0.5 to 0.95.) performance indicators. Compared with other advanced mainstream algorithms, it has more accurate recognition precision and faster detection speed, which provides strong support for early detection and management of rice leaf pests and diseases.
######
#####
License
----
The source code is free for research and education use only. Any comercial use should get formal permission first.  <br>  <br>
<br>
<a href="https://www.ultralytics.com/" target="_blank"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 📚 Ultralytics Docs

[Ultralytics](https://www.ultralytics.com/) Docs are the gateway to understanding and utilizing our cutting-edge machine learning tools. These documents are deployed to [https://docs.ultralytics.com](https://docs.ultralytics.com/) for your convenience.

[![pages-build-deployment](https://github.com/ultralytics/docs/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/ultralytics/docs/actions/workflows/pages/pages-build-deployment)
[![Check Broken links](https://github.com/ultralytics/docs/actions/workflows/links.yml/badge.svg)](https://github.com/ultralytics/docs/actions/workflows/links.yml)
[![Check Domains](https://github.com/ultralytics/docs/actions/workflows/check_domains.yml/badge.svg)](https://github.com/ultralytics/docs/actions/workflows/check_domains.yml)
[![Ultralytics Actions](https://github.com/ultralytics/docs/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/docs/actions/workflows/format.yml)

<a href="https://discord.com/invite/ultralytics"><img alt="Discord" src="https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue"></a> <a href="https://community.ultralytics.com/"><img alt="Ultralytics Forums" src="https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue"></a> <a href="https://reddit.com/r/ultralytics"><img alt="Ultralytics Reddit" src="https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue"></a>

## 🛠️ Installation

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics/)
[![Downloads](https://static.pepy.tech/badge/ultralytics)](https://www.pepy.tech/projects/ultralytics)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics/)

To install the Ultralytics package in developer mode, ensure you have Git and Python 3 installed on your system. Then, follow these steps:

1. Clone the ultralytics repository to your local machine using Git:

    ```bash
    git clone https://github.com/ultralytics/ultralytics.git
    ```

2. Navigate to the cloned repository's root directory:

    ```bash
    cd ultralytics
    ```

3. Install the package in developer mode using pip (or pip3 for Python 3):

    ```bash
    pip install -e '.[dev]'
    ```

- This command installs the Ultralytics package along with all development dependencies, allowing you to modify the package code and have the changes immediately reflected in your Python environment.

## 🚀 Building and Serving Locally

The `mkdocs serve` command builds and serves a local version of your MkDocs documentation, ideal for development and testing:

```bash
mkdocs serve
```

- #### Command Breakdown:

    - `mkdocs` is the main MkDocs command-line interface.
    - `serve` is the subcommand to build and locally serve your documentation.

- 🧐 Note:

    - Grasp changes to the docs in real-time as `mkdocs serve` supports live reloading.
    - To stop the local server, press `CTRL+C`.

## 🌍 Building and Serving Multi-Language

Supporting multi-language documentation? Follow these steps:

1. Stage all new language \*.md files with Git:

    ```bash
    git add docs/**/*.md -f
    ```

2. Build all languages to the `/site` folder, ensuring relevant root-level files are present:

    ```bash
    # Clear existing /site directory
    rm -rf site

    # Loop through each language config file and build
    mkdocs build -f docs/mkdocs.yml
    for file in docs/mkdocs_*.yml; do
      echo "Building MkDocs site with $file"
      mkdocs build -f "$file"
    done
    ```

3. To preview your site, initiate a simple HTTP server:

    ```bash
    cd site
    python -m http.server
    # Open in your preferred browser
    ```

- 🖥️ Access the live site at `http://localhost:8000`.

## 📤 Deploying Your Documentation Site

Choose a hosting provider and deployment method for your MkDocs documentation:

- Configure `mkdocs.yml` with deployment settings.
- Use `mkdocs deploy` to build and deploy your site.

* ### GitHub Pages Deployment Example:

    ```bash
    mkdocs gh-deploy
    ```

- Update the "Custom domain" in your repository's settings for a personalized URL.

![MkDocs deployment example](https://github.com/ultralytics/docs/releases/download/0/mkdocs-deployment-example.avif)

- For detailed deployment guidance, consult the [MkDocs documentation](https://www.mkdocs.org/user-guide/deploying-your-docs/).

## 💡 Contribute

We cherish the community's input as it drives Ultralytics open-source initiatives. Dive into the [Contributing Guide](https://docs.ultralytics.com/help/contributing/) and share your thoughts via our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A heartfelt thank you 🙏 to each contributor!

![Ultralytics open-source contributors](https://github.com/ultralytics/docs/releases/download/0/ultralytics-open-source-contributors.avif)

## 📜 License

Ultralytics Docs presents two licensing options:

- **AGPL-3.0 License**: Perfect for academia and open collaboration. Details are in the [LICENSE](https://github.com/ultralytics/docs/blob/main/LICENSE) file.
- **Enterprise License**: Tailored for commercial usage, offering a seamless blend of Ultralytics technology in your products. Learn more at [Ultralytics Licensing](https://www.ultralytics.com/license).

## ✉️ Contact

For Ultralytics bug reports and feature requests please visit [GitHub Issues](https://github.com/ultralytics/ultralytics/issues). Become a member of the Ultralytics [Discord](https://discord.com/invite/ultralytics), [Reddit](https://www.reddit.com/r/ultralytics/), or [Forums](https://community.ultralytics.com/) for asking questions, sharing projects, learning discussions, or for help with all things Ultralytics!

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics?sub_confirmation=1"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
