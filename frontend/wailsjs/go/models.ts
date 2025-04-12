export namespace main {
	
	export class Result {
	    Name: string;
	    Role: string;
	    Company: string;
	    Email: string;
	
	    static createFrom(source: any = {}) {
	        return new Result(source);
	    }
	
	    constructor(source: any = {}) {
	        if ('string' === typeof source) source = JSON.parse(source);
	        this.Name = source["Name"];
	        this.Role = source["Role"];
	        this.Company = source["Company"];
	        this.Email = source["Email"];
	    }
	}

}

export namespace parser {
	
	export class Prospect {
	    name: string;
	    role: string;
	    email: string;
	    company: string;
	    posted: string;
	    remote: string;
	    company_email: string;
	    linkedin: string;
	    twitter: string;
	
	    static createFrom(source: any = {}) {
	        return new Prospect(source);
	    }
	
	    constructor(source: any = {}) {
	        if ('string' === typeof source) source = JSON.parse(source);
	        this.name = source["name"];
	        this.role = source["role"];
	        this.email = source["email"];
	        this.company = source["company"];
	        this.posted = source["posted"];
	        this.remote = source["remote"];
	        this.company_email = source["company_email"];
	        this.linkedin = source["linkedin"];
	        this.twitter = source["twitter"];
	    }
	}

}

