# SupaStudy

**Your study space.**

SupaStudy is a student planning app in active development. Its goal is to turn teaching schedules into organized courses, calendar events, and reminders. Development currently focuses on a responsive web experience built with Expo, while retaining a shared foundation for future iOS and Android apps.

## Current status

- Responsive UI prototype with a shared theme, logo, and icon navigation.
- Desktop navigation and a separate bottom navigation bar on smaller screens.
- Python command-line document extraction using Gemini, with fallback models.
- Structured JSON output with source filename, processing timestamp, and entry count.
- A separate Gemini evaluator using DeepEval G-Eval, run automatically after extraction. Its score and explanation are printed in the terminal.

Navigation currently changes the selected button; it does not yet open complete course or calendar screens. The Python pipeline is not connected to the web UI or exposed as a hosted API.

## Planned features

- PDF upload from the application.
- An interactive calendar populated from extracted schedules.
- Course management, reminders, and persistent database storage.
- Word document support and review of ambiguous extracted information.
- Further native iOS and Android development.

## Technology

- Expo SDK 58, React Native, React, TypeScript, and Expo Router.
- React Native Web, Expo Blur, and Expo Symbols for the interface.
- Python, Google Gen AI SDK, python-dotenv, and DeepEval for AI processing.
- pdfplumber for the earlier table-based PDF extraction experiments.
- ESLint, TypeScript, Jest, and React Native Testing Library for development checks.

## Run the web app

Install Node.js compatible with the Expo version in package.json and npm. From the repository root:

```bash
npm ci
npm run web
```

Open the URL printed by Expo. For the Expo development menu, use `npm start`. Native development commands are `npm run ios` and `npm run android`; these require the corresponding local simulator or emulator setup.

## Run document extraction

The current AI extractor accepts PDF, PNG, JPG, and JPEG files up to 15 MB. It does not currently accept Word documents. Python 3.13 has been used during development.

On macOS or Linux, from the repository root:

```bash
python3 -m venv backend/.venv
source backend/.venv/bin/activate
python -m pip install google-genai python-dotenv deepeval pdfplumber
```

Python dependencies are not yet pinned in a requirements file, so a new installation may require compatibility adjustments.

Create `backend/.env` locally:

```dotenv
GEMINI_API_KEY=your_api_key_here
```

Optionally set `GEMINI_EVALUATION_MODEL` to an available Gemini model supported by your account. Extraction models are listed in `backend/ai_extractor.py`; the evaluator default is defined in `backend/evaluate_schedule.py`. Availability and quotas depend on the provider and account; free access is not guaranteed by this project.

Run:

```bash
python backend/inspect_ai.py
```

Enter the path to a supported document when prompted. The script extracts the schedule, saves a uniquely named JSON file under `results/`, and then evaluates it against the original document. The results directory is created automatically. Evaluation failure does not delete the saved extraction.

Dates in schedule output use `DD.MM.YYYY`; times use `HH:MM`. JSON field names are English while extracted source content retains its original language. Missing or ambiguous information should be represented explicitly rather than invented.

Documents are sent to the configured cloud models. The evaluator score is an AI assessment, not a statistically verified accuracy percentage or a guarantee that the data is correct. Review important dates before relying on them.

## Project structure

```text
src/
  app/                 Screens and root layout
  components/Navbar/   Navbar component and styles
  hooks/               Shared React hooks
  styles/              Theme and shared styles
assets/                Branding, icons, and images
backend/
  inspect_ai.py        Command-line entry point
  ai_extractor.py      Document extraction and model fallback
  schedule_schema.py   Structured extraction schema
  result_builder.py    Output metadata
  json_storage.py      JSON persistence
  evaluate_schedule.py AI evaluation
  manual_scripts/      Earlier PDF table extraction experiments
__tests__/             Frontend tests
results/               Local generated output (ignored)
test_documents/        Local sample documents (ignored)
```

The scripts under `manual_scripts` are experimental legacy tools and are not the supported entry point for the AI workflow.

## Design

The visual identity uses a teal primary color (`#286C64`), dark text, a neutral gray page background, and lighter teal accents. Shared values live in `src/styles/theme.ts`; component-specific styles live alongside their components. Literata and IBM Plex Sans are the planned typography choices.

## Development checks

```bash
npm run lint
npx tsc --noEmit
npm test -- --watchAll=false
```

The existing starter screen test still expects `Welcome!` and needs updating for the current UI. Do not treat the test suite as a complete verification of the application.

## Deploy the web prototype to Vercel

The app uses `web.output: "static"` in `app.json`.

- Root directory: `./`
- Framework preset: `Other`
- Install command: `npm ci`
- Build command: `npx expo export --platform web`
- Output directory: `dist`

To verify the export locally:

```bash
npx expo export --platform web
```

This deploys the frontend only. Python scripts are not automatically deployed as an API, and local JSON files are not a production database. No environment variables are required for the current UI. Never expose Gemini keys through `EXPO_PUBLIC_` variables.

## Repository hygiene

Keep credentials in ignored local environment files. Dependencies, build output, Python environments, caches, generated JSON results, local input documents, and local AI tooling files are excluded by `.gitignore`. Keep application source, assets, configuration, and `package-lock.json` in version control.

## License

See [LICENSE](LICENSE). The repository currently retains the MIT license notice from the Expo starter.
