# Open Source Project Template (Gauthier)

Starter template for building and publishing open source projects with a clean structure and community standards already in place.

![Capture](/docs/images/Capture.png)

## What this template includes

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

## Repository structure

```text
open-source-template/
├── dashboard/
│   ├── requirements.txt
│   └── streamlit_app.py
├── docs/
│   └── images/
├── .gitignore
├── ACKNOWLEDGEMENTS.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
├── README.md
└── SECURITY.md
```

## Quick start

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

## Optional local setup (Streamlit)

If you use the `dashboard/` app:

```bash
pip install -r dashboard/requirements.txt
streamlit run dashboard/streamlit_app.py
```

## Customization checklist

- Project name and one-sentence description
- Installation instructions
- Usage examples
- Maintainers / contact information
- Roadmap (optional)
- Badges (CI, coverage, release)

## Contributing

See [CONTRIBUTING.md](/CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](/CODE_OF_CONDUCT.md).

## Security

See [SECURITY.md](/SECURITY.md) for vulnerability reporting guidelines.

## Changelog

Track all notable project changes in [CHANGELOG.md](/CHANGELOG.md).

Recommended:
- Follow a consistent format such as Keep a Changelog
- Create an entry for each release
- Include Added, Changed, Fixed, and Removed sections when relevant

## Acknowledgements

Use [ACKNOWLEDGEMENTS.md](/ACKNOWLEDGEMENTS.md) to credit people, tools, libraries, and communities that helped the project.

## License

See [LICENSE.md](/LICENSE.md).

## Author

Gauthier Rammault
