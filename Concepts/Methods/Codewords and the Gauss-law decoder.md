---
type: "concept"
tags: ["concept"]
aliases: ["decoder", "codewords"]
as_of: "2026-10-05"
---
# Codewords and the Gauss-law decoder

**Plain words.** Each physical state is assigned a fixed bit string (its *codeword*; 12 bits at 2×2). After
measurement, the decoder checks every string against [[Gauss's law]] and link consistency and either returns the
physical state or rejects the string. Random strings pass only ~0.15 % of the time, so the codewords act as a
built-in distance-2 error-*detection* code. Code: [[skqd.codec]].
