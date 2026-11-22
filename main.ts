// Entry program for the make.fun bounty gta6-meme-x-01 (Node 22, stdlib only).
//
// The entry itself is a post on X: a GTA 6 meme whose picture carries the
// make.fun ghost and whose text carries the bounty link and a play code.
// This repository only has to name that post, so the program's single job is
// to copy POST.json from the repository root into the output directory,
// where the make.fun gate picks it up and reads the post from X itself.
//
// Locally, MAKEFUN_OUTPUT_DIR points at the output directory; inside the
// grader it defaults to /output:
//   MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outputDir, { recursive: true });
copyFileSync(join(repoRoot, "POST.json"), join(outputDir, "POST.json"));
console.log(`POST.json copied to ${join(outputDir, "POST.json")}`);
