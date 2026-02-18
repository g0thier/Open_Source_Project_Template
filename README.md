# Open Source Project Template (Gauthier)

## Description

Starter template for building and publishing open source projects with a clean structure and community standards already in place.

![Capture](/docs/images/Capture.png)

## Table of Contents

- [Open Source Project Template (Gauthier)](#open-source-project-template-gauthier)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [🎯 Objective of the project](#-objective-of-the-project)
  - [👥 Target audience](#-target-audience)
  - [⚙️ What this template includes](#️-what-this-template-includes)
  - [🗂️ Repository structure](#️-repository-structure)
  - [🚀 Quick start](#-quick-start)
  - [🐳 Install \& execute](#-install--execute)
  - [🥽 Security](#-security)
  - [📰 Changelog](#-changelog)
  - [🩷 Acknowledgements](#-acknowledgements)
    - [Environnement](#environnement)
  - [🧪 Project Status](#-project-status)
  - [🔒 License](#-license)
  - [🤝 Contributing](#-contributing)
  - [👤 Author](#-author)

## 🎯 Objective of the project

Facilitate and Accelerate project creation.

## 👥 Target audience 

- Python Developers 
- Students in mathematics / computer science

## ⚙️ What this template includes

- `.gitignore` for macOS configuration
- Core community files:
  - `CODE_OF_CONDUCT.md`
  - `CONTRIBUTING.md`
  - `SECURITY.md`
  - `CHANGELOG.md`
  - `LICENSE.md`
  - `ACKNOWLEDGEMENTS.md`
- Optional Streamlit starter app in `dashboard/`
- Basic documentation assets in `docs/`

## 🗂️ Repository structure

```text
open-source-template/
├── dashboard/
│   ├── requirements.txt
│   └── streamlit_app.py
├── docs/
│   └── images/
├── notebooks/
│   └── notebooks.ipynb
├── .gitignore
├── ACKNOWLEDGEMENTS.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
├── README.md
└── SECURITY.md
```

## 🚀 Quick start

1. Use this folder as a base for your new open source project.
2. Rename the project and update this `README.md`.
3. Replace placeholder content in:
   - `CONTRIBUTING.md`
   - `SECURITY.md`
   - `CHANGELOG.md`
   - `ACKNOWLEDGEMENTS.md`
   - `LICENSE.md` (if needed)
4. Add your source code and project-specific docs.
5. Publish and maintain the repository using your contribution workflow.

## 🐳 Install & execute

If you use the `dashboard/` app:

```bash
pip install -r dashboard/requirements.txt
streamlit run dashboard/streamlit_app.py
```

If you use the `fastapi/` app:

```bash
pip install -r fastapi/requirements.txt
cd fastapi/app
fastapi dev main.py
```

## 🥽 Security

- See [SECURITY.md](/SECURITY.md) for vulnerability reporting guidelines.

## 📰 Changelog

Track all notable project changes in [CHANGELOG.md](/CHANGELOG.md).

Recommended:
- Follow a consistent format such as Keep a Changelog
- Create an entry for each release
- Include Added, Changed, Fixed, and Removed sections when relevant

## 🩷 Acknowledgements

- Use [ACKNOWLEDGEMENTS.md](/ACKNOWLEDGEMENTS.md) to credit people, tools, libraries, and communities that helped the project.

### Environnement

- **Python ≥ 3.13.5**
- Dependencies listed in [requirements.txt](/dashboard/requirements.txt)

## 🧪 Project Status

- 🔬 **Statut** : experimental
- 🧭 **Roadmap** : to be defined

## 🔒 License

- See [LICENSE.md](/LICENSE.md).

## 🤝 Contributing

Contributions are welcome.
- See [CONTRIBUTING.md](/CONTRIBUTING.md)
- Code of conduct available in [CODE_OF_CONDUCT.md](/CODE_OF_CONDUCT.md).

## 👤 Author

Gauthier Rammault
