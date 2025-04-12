<script>
	import { StartScan, ExportToCSV, ExportToSheets } from '../wailsjs/go/main/App';

	let jobSource = "Y Combinator";
	let useHunter = true;
	let useApollo = false;
	let results = [];

	async function startScan() {
		console.log("🚨 Start button clicked");

		try {
			results = await StartScan(jobSource, useHunter, useApollo);
			console.log("✅ Got results:", results);
		} catch (err) {
			console.error("❌ Failed to call Go:", err);
			alert("StartScan failed.");
		}
	}

	async function exportCSV() {
		console.log("📤 Export to CSV clicked");

		if (!results || results.length === 0) {
			alert("No data to export.");
			return;
		}

		try {
			await ExportToCSV(results);
			alert("✅ CSV saved in devapply folder!");
		} catch (err) {
			console.error("❌ CSV export failed:", err);
			alert("Failed to export CSV.");
		}
	}

	async function exportToGoogleSheets() {
		console.log("📤 Export to Google Sheets clicked");

		if (!results || results.length === 0) {
			alert("No data to export.");
			return;
		}

		try {
			await ExportToSheets(results);
			alert("✅ Sent to Google Sheets!");
		} catch (err) {
			console.error("❌ Sheets export failed:", err);
			alert("❌ Failed to export to Google Sheets.");
		}
	}
</script>

<style>
	body {
		background: #1b2636;
		color: white;
		font-family: sans-serif;
		padding: 2rem;
	}
	table {
		width: 100%;
		margin-top: 1rem;
		border-collapse: collapse;
	}
	th, td {
		border: 1px solid #444;
		padding: 0.5rem;
	}
	button {
		margin-top: 1rem;
		padding: 0.5rem 1rem;
		cursor: pointer;
		background: #333;
		color: white;
		border: none;
		border-radius: 4px;
	}
	select, input[type="checkbox"] {
		margin-left: 0.5rem;
	}
</style>

<h1>DevApply Config</h1>

<div>
	<label for="jobSource">Select Job Source:</label>
	<select bind:value={jobSource} id="jobSource">
		<option>Y Combinator</option>
		<option>LinkedIn</option>
		<option>Hacker News</option>
	</select>
</div>

<div>
	<label><input type="checkbox" bind:checked={useHunter}> Use Hunter.io</label>
</div>

<div>
	<label><input type="checkbox" bind:checked={useApollo}> Use Apollo</label>
</div>

<button on:click={() => startScan()}>Start</button>

{#if results.length > 0}
	<h2>🧠 Scraped Results</h2>
	<table>
		<thead>
			<tr>
				<th>Name</th>
				<th>Role</th>
				<th>Company</th>
				<th>Email</th>
			</tr>
		</thead>
		<tbody>
			{#each results as r}
				<tr>
					<td>{r.Name ?? '—'}</td>
					<td>{r.Role ?? '—'}</td>
					<td>{r.Company ?? '—'}</td>
					<td>{r.Email ?? '—'}</td>
				</tr>
			{/each}
		</tbody>
	</table>

	<!-- EXPORT BUTTONS -->
	<button on:click={() => exportCSV()}>Export to CSV</button>
	<button on:click={() => exportToGoogleSheets()}>Export to Google Sheets</button>
{/if}


