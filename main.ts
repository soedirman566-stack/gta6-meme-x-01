// Hand-in program for the make.fun gta6-meme-x-01 entry.
// The entry itself is a post on X; this repository only names it.
// POST.json at the repo root holds the post's URL, and handing in
// means delivering that file to the output directory, unchanged.

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Where this program lives is the repository root.
const repoRoot = dirname(fileURLToPath(import.meta.url));

// The grader sets MAKEFUN_OUTPUT_DIR; fall back to /output.
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

// Make sure the destination exists, then copy the post file over.
mkdirSync(outputDir, { recursive: true });
const destination = join(outputDir, "POST.json");
copyFileSync(join(repoRoot, "POST.json"), destination);

console.log(`POST.json copied to ${destination}`);
